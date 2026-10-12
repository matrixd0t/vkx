import unittest

import vkx.models as models
from vkx.models.events import bot_events, user_events
from vkx.models.events.objects import group_event_objects, user_event_objects


class ModelsExportsTests(unittest.TestCase):
    def test_all_entries_exist(self):
        missing = [name for name in models.__all__ if not hasattr(models, name)]
        self.assertEqual(missing, [])

    def test_group_event_objects_reexported(self):
        missing = [
            name for name in group_event_objects.__all__ if not hasattr(models, name)
        ]
        self.assertEqual(missing, [])
        self.assertIs(models.MessageEventObject, group_event_objects.MessageEventObject)

    def test_user_event_objects_reexported(self):
        missing = [
            name for name in user_event_objects.__all__ if not hasattr(models, name)
        ]
        self.assertEqual(missing, [])

    def test_user_events_reexported(self):
        missing = [name for name in user_events.__all__ if not hasattr(models, name)]
        self.assertEqual(missing, [])

    def test_group_versions_win_collisions(self):
        self.assertIs(models.MessageNewObject, group_event_objects.MessageNewObject)
        self.assertIs(models.MessageEditObject, group_event_objects.MessageEditObject)
        self.assertIs(models.MessageNewEvent, bot_events.MessageNewEvent)
        self.assertIs(models.MessageEditEvent, bot_events.MessageEditEvent)


if __name__ == "__main__":
    unittest.main()
