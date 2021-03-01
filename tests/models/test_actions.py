import unittest
from sqlalchemy.exc import IntegrityError

from api import create_app, db
from api.database.models.quests import Quest
from api.database.models.encounters import Encounter
from api.database.models.actions import Action

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

    def test_action_model(self):
        quest = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active' )
        quest.insert()

        encounter_1 = Encounter(monster_image='https://images.huffingtonpost.com/2015-02-05-trollersTroll-thumb.jpg', quest_id=quest.id, progress=1)
        encounter_1.insert()

        action_1 = Action(encounter_id=encounter_1.id,  description='Send a message to a recruiter')
        action_1.insert()

        self.assertIsInstance(action_1, Action)
        self.assertIsNotNone(action_1.id)
        self.assertEqual('Send a message to a recruiter', action_1.description)
        self.assertEqual(encounter_1.id, action_1.encounter_id)

    def test_action_model_blank_description(self):
        try:
            quest = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active' )
            quest.insert()

            encounter_1 = Encounter(monster_image='https://images.huffingtonpost.com/2015-02-05-trollersTroll-thumb.jpg', quest_id=quest.id, progress=1)
            encounter_1.insert()

            action_1 = Action(encounter_id=encounter_1.id,  description='')
            action_1.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            # we should not end up in here
            self.assertTrue(False)  # pragma: no cover

    def test_encounter_model_missing_description(self):
        try:
            quest = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active' )
            quest.insert()

            encounter_1 = Encounter(monster_image='https://images.huffingtonpost.com/2015-02-05-trollersTroll-thumb.jpg', quest_id=quest.id, progress=1)
            encounter_1.insert()

            action_1 = Action(encounter_id=encounter_1.id,  description=None)
            action_1.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            # we should not end up in here
            self.assertTrue(False)  # pragma: no cover
