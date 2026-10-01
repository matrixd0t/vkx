[CmdletBinding()]
param(
    [switch]$SkipChecks
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Remote = "origin"
$DevelopmentBranch = "dev"
$ProductionBranch = "master"
$Repository = "matrixd0t/vkx"
$PackageName = "vkx"
$ProjectFile = Join-Path $PSScriptRoot "pyproject.toml"
$MaximumMergeWaitAttempts = 360
$MergeWaitSeconds = 5

function Write-Step {
    param([Parameter(Mandatory = $true)][string]$Message)
    Write-Host ""
    Write-Host "==> $Message" -ForegroundColor Cyan
}

function Invoke-Checked {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath,
        [string[]]$ArgumentList = @()
    )

    & $FilePath @ArgumentList
    if ($LASTEXITCODE -ne 0) {
        throw "$FilePath failed with exit code $LASTEXITCODE"
    }
}

function Get-CheckedOutput {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath,
        [string[]]$ArgumentList = @()
    )

    $output = & $FilePath @ArgumentList
    if ($LASTEXITCODE -ne 0) {
        throw "$FilePath failed with exit code $LASTEXITCODE"
    }
    return ($output | Out-String).Trim()
}

function Get-VersionFromText {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Text
    )

    $match = [regex]::Match($Text, '(?m)^\s*version\s*=\s*"([^"]+)"\s*$')
    if (-not $match.Success) {
        throw "Could not find project version"
    }
    return $match.Groups[1].Value
}

function Get-ProjectVersion {
    return Get-VersionFromText (Get-Content -LiteralPath $ProjectFile -Raw)
}

function Test-CommitAncestor {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Ancestor,
        [Parameter(Mandatory = $true)]
        [string]$Descendant
    )

    & git @("merge-base", "--is-ancestor", $Ancestor, $Descendant) *> $null
    return $LASTEXITCODE -eq 0
}

function Test-VersionPublished {
    param([Parameter(Mandatory = $true)][string]$Version)

    try {
        Invoke-RestMethod -Uri "https://pypi.org/pypi/$PackageName/$Version/json" -Method Head *> $null
        return $true
    }
    catch {
        $statusCode = $null
        if ($null -ne $_.Exception.Response) {
            $statusCode = [int]$_.Exception.Response.StatusCode
        }
        if ($statusCode -eq 404) {
            return $false
        }
        Write-Warning "Could not check PyPI for $PackageName $Version ($($_.Exception.Message)); continuing."
        return $false
    }
}

Write-Host "!!! IMPORTANT !!! CHECK IF YOU'VE FORGOT TO CHANGE THE LIBRARY VERSION !!! (uv version --bump patch)" -ForegroundColor Yellow

if ($null -eq (Get-Command uv -ErrorAction SilentlyContinue)) {
    throw "Required command is not available: uv"
}

foreach ($command in @("git", "gh")) {
    if ($null -eq (Get-Command $command -ErrorAction SilentlyContinue)) {
        throw "Required command is not available: $command"
    }
}

if (-not (Test-Path -LiteralPath $ProjectFile)) {
    throw "Project file was not found: $ProjectFile"
}

$branch = Get-CheckedOutput git @("branch", "--show-current")
if ($branch -ne $DevelopmentBranch) {
    throw "Release must start on '$DevelopmentBranch', current branch is '$branch'"
}

$worktree = Get-CheckedOutput git @("status", "--porcelain")
if (-not [string]::IsNullOrWhiteSpace($worktree)) {
    throw "Working tree is not clean. Commit or stash existing changes first."
}

Invoke-Checked gh @("auth", "status")

$releaseVersion = Get-ProjectVersion
if (Test-VersionPublished $releaseVersion) {
    throw "$PackageName $releaseVersion is already published on PyPI. Bump the version first (uv version --bump patch)."
}

if (-not $SkipChecks) {
    Write-Step "Running lint"
    Invoke-Checked uv @("run", "ruff", "check", "src")

    Write-Step "Running type check"
    Invoke-Checked uvx @("pyright")

    Write-Step "Verifying the build"
    Invoke-Checked uv @("build")
}

Write-Step "Checking branches"
Invoke-Checked git @("fetch", $Remote, $DevelopmentBranch, $ProductionBranch)

if (-not (Test-CommitAncestor "$Remote/$DevelopmentBranch" $DevelopmentBranch)) {
    if (Test-CommitAncestor $DevelopmentBranch "$Remote/$DevelopmentBranch") {
        throw "Local '$DevelopmentBranch' is behind '$Remote/$DevelopmentBranch'. Update it before releasing."
    }

    throw "Local '$DevelopmentBranch' and '$Remote/$DevelopmentBranch' have diverged. If the local branch was intentionally rebased, run 'git push --force-with-lease $Remote $DevelopmentBranch' first."
}

if (-not (Test-CommitAncestor "$Remote/$ProductionBranch" "$Remote/$DevelopmentBranch")) {
    throw "Remote '$ProductionBranch' is not an ancestor of '$DevelopmentBranch'. Synchronize '$DevelopmentBranch' with '$ProductionBranch' before releasing."
}

Invoke-Checked git @("diff", "--check")

Write-Step "Pushing '$DevelopmentBranch'"
Invoke-Checked git @("push", $Remote, $DevelopmentBranch)
$developmentHeadBeforeMerge = Get-CheckedOutput git @("rev-parse", "$Remote/$DevelopmentBranch")

$openPrJson = Get-CheckedOutput gh @(
    "pr",
    "list",
    "--repo",
    $Repository,
    "--base",
    $ProductionBranch,
    "--head",
    $DevelopmentBranch,
    "--state",
    "open",
    "--limit",
    "1",
    "--json",
    "number,url"
)

$pr = $null
if (-not [string]::IsNullOrWhiteSpace($openPrJson)) {
    $parsedPrs = ConvertFrom-Json -InputObject $openPrJson
    foreach ($candidate in @($parsedPrs)) {
        if ($null -eq $candidate) {
            continue
        }

        $numberProperty = $candidate.PSObject.Properties["number"]
        $urlProperty = $candidate.PSObject.Properties["url"]
        if ($null -ne $numberProperty -and $null -ne $urlProperty) {
            $pr = $candidate
            break
        }
    }
}

if ($null -eq $pr) {
    $prTitle = "Release vkx $releaseVersion"
    $prBody = @"
Automated release for vkx $releaseVersion.

The package will be published by GitHub Actions after this PR is merged into $ProductionBranch.
"@
    $prUrl = Get-CheckedOutput gh @(
        "pr",
        "create",
        "--repo",
        $Repository,
        "--base",
        $ProductionBranch,
        "--head",
        $DevelopmentBranch,
        "--title",
        $prTitle,
        "--body",
        $prBody
    )
    $prNumber = Get-CheckedOutput gh @(
        "pr",
        "view",
        $prUrl,
        "--repo",
        $Repository,
        "--json",
        "number",
        "--jq",
        ".number"
    )
}
else {
    $prNumber = [string]$pr.number
    $prUrl = [string]$pr.url
}

Write-Host "Release PR: $prUrl"
$checkStatusJson = Get-CheckedOutput gh @(
    "pr",
    "view",
    $prNumber,
    "--repo",
    $Repository,
    "--json",
    "statusCheckRollup"
)
$checkStatus = ConvertFrom-Json -InputObject $checkStatusJson
$checkRuns = @()
if ($null -ne $checkStatus -and $null -ne $checkStatus.statusCheckRollup) {
    $checkRuns = @($checkStatus.statusCheckRollup)
}

if ($checkRuns.Count -eq 0) {
    Write-Host "No PR checks reported; continuing with merge."
}
else {
    Invoke-Checked gh @(
        "pr",
        "checks",
        $prNumber,
        "--repo",
        $Repository,
        "--watch"
    )
}

Invoke-Checked gh @(
    "pr",
    "merge",
    $prNumber,
    "--repo",
    $Repository,
    "--rebase"
)

$merged = $false
for ($attempt = 0; $attempt -lt $MaximumMergeWaitAttempts; $attempt++) {
    $prStateJson = Get-CheckedOutput gh @(
        "pr",
        "view",
        $prNumber,
        "--repo",
        $Repository,
        "--json",
        "state,mergedAt"
    )
    $prState = $prStateJson | ConvertFrom-Json
    if ($prState.state -eq "MERGED") {
        $merged = $true
        break
    }
    if ($prState.state -eq "CLOSED") {
        throw "Release PR was closed without being merged: $prUrl"
    }
    Start-Sleep -Seconds $MergeWaitSeconds
}

if (-not $merged) {
    throw "Release PR was not merged within the configured timeout: $prUrl"
}

Invoke-Checked git @("fetch", $Remote, $ProductionBranch, $DevelopmentBranch)
$masterProjectFile = Get-CheckedOutput git @("show", "${Remote}/${ProductionBranch}:pyproject.toml")
$masterVersion = Get-VersionFromText $masterProjectFile
if ($masterVersion -ne $releaseVersion) {
    throw "$ProductionBranch contains version $masterVersion instead of $releaseVersion"
}

Invoke-Checked git @("switch", $ProductionBranch)
Invoke-Checked git @("pull", "--ff-only", $Remote, $ProductionBranch)

$productionHead = Get-CheckedOutput git @("rev-parse", $ProductionBranch)
$developmentHead = Get-CheckedOutput git @("rev-parse", "$Remote/$DevelopmentBranch")
if ($developmentHead -ne $productionHead -and $developmentHead -ne $developmentHeadBeforeMerge) {
    throw "Remote '$DevelopmentBranch' changed while the release PR was merging. Refusing to overwrite it."
}

# GitHub's rebase merge rewrites the PR commits on master and leaves dev behind.
Invoke-Checked git @("branch", "--force", $DevelopmentBranch, $productionHead)
if ($developmentHead -ne $productionHead) {
    $forceLease = "--force-with-lease=refs/heads/{0}:{1}" -f $DevelopmentBranch, $developmentHeadBeforeMerge
    Invoke-Checked git @("push", $forceLease, $Remote, $DevelopmentBranch)
}

Invoke-Checked git @("switch", $DevelopmentBranch)

Write-Host ""
Write-Host "Released $PackageName $releaseVersion. GitHub Actions will publish it to PyPI." -ForegroundColor Green
Write-Host "Watch the run: gh run list --repo $Repository --workflow publish.yml" -ForegroundColor Green
