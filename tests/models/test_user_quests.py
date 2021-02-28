import unittest
from sqlalchemy.exc import IntegrityError

from api import create_app, db
from api.database.models.users import User
from api.database.models.quests import Quest
from api.database.models.user_quests import UserQuest

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

    def test_user_quest_model(self):
        user = User(username='ian', email='ian.douglas@iandouglas.com', xp=0)
        user.insert()
        quest_1 = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active')
        quest_2 = Quest(name="Make'a da biscuit!", xp=10, level=2, encounter_req=1, type='active')
        db.session.add(quest_1)
        db.session.add(quest_2)
        db.session.commit()

        user_quest_1 = UserQuest(quest_id=quest_1.id, user_id=user.id, progress=1, completion_status=False)
        user_quest_2 = UserQuest(quest_id=quest_2.id, user_id=user.id, progress=1, completion_status=False)
        user_quest_1.insert()
        user_quest_2.insert()

        self.assertIsInstance(user_quest_1, UserQuest)
        self.assertEqual(UserQuest.query.count(), 2)

        self.assertIsNotNone(user_quest_1.id)
        self.assertEqual(1, user.id)
        self.assertEqual(user.id, user_quest_1.user_id)
        self.assertEqual(user.id, user_quest_2.user_id)
        self.assertEqual(1, user_quest_1.progress)
        self.assertEqual(False, user_quest_1.completion_status)

    def test_user_quest_can_update_attributes(self):
        user = User(username='ian', email='ian.douglas@iandouglas.com', xp=0)
        user.insert()
        quest_1 = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active')
        db.session.add(quest_1)
        db.session.commit()

        user_quest_1 = UserQuest(quest_id=quest_1.id, user_id=user.id, progress=1, completion_status=False)
        user_quest_1.insert()

        self.assertEqual(1, user_quest_1.progress)

        user_quest_1 = UserQuest(quest_id=quest_1.id, user_id=user.id, progress=2, completion_status=False)
        user_quest_1.update()

        self.assertEqual(2, user_quest_1.progress)
