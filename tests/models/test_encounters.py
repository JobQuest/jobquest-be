import unittest
from sqlalchemy.exc import IntegrityError

from api import create_app, db
from api.database.models.quests import Quest
from api.database.models.encounters import Encounter


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

    def test_encounter_model(self):
        quest = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active' )
        quest.insert()

        encounter_1 = Encounter(monster_image='https://images.huffingtonpost.com/2015-02-05-trollersTroll-thumb.jpg', quest_id=quest.id, progress=1)
        encounter_1.insert()

        self.assertIsInstance(encounter_1, Encounter)
        self.assertIsNotNone(encounter_1.id)
        self.assertEqual('https://images.huffingtonpost.com/2015-02-05-trollersTroll-thumb.jpg', encounter_1.monster_image)
        self.assertEqual(quest.id, encounter_1.quest_id)
        self.assertEqual(1, encounter_1.progress)

    def test_encounter_model_blank_monster_image(self):
        try:
            quest = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active' )
            quest.insert()

            encounter_1 = Encounter(monster_image='', quest_id=quest.id, progress=1)
            encounter_1.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            # we should not end up in here
            self.assertTrue(False)  # pragma: no cover

    def test_encounter_model_missing_monster_image(self):
        try:
            quest = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active' )
            quest.insert()

            encounter_1 = Encounter(monster_image=None, quest_id=quest.id, progress=1)
            encounter_1.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            # we should not end up in here
            self.assertTrue(False)  # pragma: no cover

    def test_encounter_model_can_update_attributes(self):
        quest = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active' )
        quest.insert()

        encounter_1 = Encounter(monster_image='https://images.huffingtonpost.com/2015-02-05-trollersTroll-thumb.jpg', quest_id=quest.id, progress=1)
        encounter_1.insert()

        self.assertEqual(1, encounter_1.progress)

        encounter_1 = Encounter(monster_image='https://images.huffingtonpost.com/2015-02-05-trollersTroll-thumb.jpg', quest_id=quest.id, progress=2)
        encounter_1.update()

        self.assertEqual(2, encounter_1.progress)
