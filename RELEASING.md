# Релиз

Публикация идёт автоматически: `release.ps1` вливает `dev` в `master`, а GitHub Actions
(`.github/workflows/publish.yml`) собирает и публикует пакет на PyPI через
[Trusted Publishing](https://docs.pypi.org/trusted-publishers/).

## Разовая настройка PyPI

1. Зарегистрируйте «pending publisher» на https://pypi.org/manage/account/publishing/:
   - **PyPI Project Name**: `vkx`
   - **Owner**: `matrixd0t`
   - **Repository name**: `vkx`
   - **Workflow name**: `publish.yml`
   - **Environment name**: `pypi`
2. Убедитесь, что в репозитории есть environment `pypi` (Settings → Environments).

Больше секретов хранить не нужно: публикация выполняется по OIDC.

## Выпуск версии

```powershell
uv version --bump patch   # или minor / major, либо вручную в pyproject.toml
git add pyproject.toml uv.lock
git commit -m "Bump version to X.Y.Z"
git push
./release.ps1
```

Скрипт проверит, что:

- текущая ветка — `dev`, дерево чистое, `gh` авторизован;
- версия из `pyproject.toml` ещё не опубликована на PyPI;
- проходят `ruff`, `pyright` и `uv build` (можно пропустить флагом `-SkipChecks`);
- `dev` не разошлась с `origin` и `master` является её предком.

Затем скрипт пушит `dev`, открывает (или переиспользует) PR в `master`, дожидается
CI, вливает rebase-merge, проверяет версию в `master` и синхронизирует `dev`.

После мержа Actions публикует релиз на PyPI. Следить за прогоном:

```powershell
gh run list --repo matrixd0t/vkx --workflow publish.yml
```
