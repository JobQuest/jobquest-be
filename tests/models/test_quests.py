import unittest
from sqlalchemy.exc import IntegrityError

from api import create_app, db
from api.database.models.quests import Quest

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_quest_model(self):
        quest = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active' )
        quest.insert()

        self.assertIsInstance(quest, Quest)
        self.assertIsNotNone(quest.id)
        self.assertEqual("Make'a da pancake!", quest.name)
        self.assertEqual(5, quest.xp)
        self.assertEqual(1, quest.level)
        self.assertEqual(3, quest.encounter_req)
        self.assertEqual('active', quest.type)

    def test_quest_model_blank_name(self):
        try:
            quest = Quest(name='', xp=0, level=1, encounter_req=3, type='active')
            quest.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            # we should not end up in here
            self.assertTrue(False)  # pragma: no cover

    def test_quest_model_missing_name(self):
        try:
            quest = Quest(name=None, xp=0, level=1, encounter_req=3, type='active')
            quest.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            # we should not end up in here
            self.assertTrue(False)  # pragma: no cover

    def test_quest_model_blank_type(self):
        try:
            quest = Quest(name="Make'a da pancake!", xp=0, level=1, encounter_req=3, type='')
            quest.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            # we should not end up in here
            self.assertTrue(False)  # pragma: no cover

    def test_quest_model_missing_type(self):
        try:
            quest = Quest(name="Make'a da pancake!", xp=0, level=1, encounter_req=3, type=None)
            quest.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            # we should not end up in here
            self.assertTrue(False)  # pragma: no cover
