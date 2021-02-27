import json
import unittest
from unittest.mock import patch
from copy import deepcopy
from api import create_app, db
from api.database.models.users import User
from api.database.models.quests import Quest
from api.database.models.user_quests import UserQuest
from tests import db_drop_everything, assert_payload_field_type_value, \
    assert_payload_field_type

class GetQuestsTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

        self.user_1 = User(username='George', email="george@example.com", xp=1000000000)
        self.user_1.insert()
        self.quest_1 = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active')
        self.quest_2 = Quest(name="Make'a da biscuit!", xp=10, level=2, encounter_req=3, type='active')
        self.quest_3 = Quest(name="Make'a da nuggets!", xp=10, level=2, encounter_req=3, type='active')
        self.quest_4 = Quest(name="Make'a da cupcake!", xp=10, level=2, encounter_req=3, type='passive')
        self.quest_5 = Quest(name="Make'a da pizza!", xp=10, level=2, encounter_req=3, type='passive')
        self.quest_6 = Quest(name="Make'a da bacon!", xp=10, level=2, encounter_req=3, type='passive')
        self.quest_7 = Quest(name="Make'a da pie!", xp=10, level=2, encounter_req=3, type='supportive')
        db.session.add(self.quest_1)
        db.session.commit()
        db.session.add(self.quest_2)
        db.session.commit()
        db.session.add(self.quest_3)
        db.session.add(self.quest_4)
        db.session.add(self.quest_5)
        db.session.add(self.quest_6)
        db.session.add(self.quest_7)
        db.session.commit()

        self.user_quest_1 = UserQuest(quest_id=self.quest_1.id, user_id=self.user_1.id, progress=1, completion_status=False)
        self.user_quest_2 = UserQuest(quest_id=self.quest_2.id, user_id=self.user_1.id, progress=1, completion_status=True)
        db.session.add(self.user_quest_1)
        db.session.commit()
        db.session.add(self.user_quest_2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db_drop_everything(db)
        self.app_context.pop()

    def test_happy_path_get_quests_for_user_true(self):
        response = self.client.get(f'/api/v1/users/{self.user_1.id}/quests?completion_status=true', content_type='application/json')

        self.assertEqual(200, response.status_code)

        data = json.loads(response.data.decode('utf-8'))

        assert_payload_field_type(self, data, 'data', dict)

        all_quest_data = data['data']

        assert_payload_field_type_value(self, all_quest_data, 'id', str, 'Null')
        assert_payload_field_type_value(self, all_quest_data, 'type', str, 'quests')

        attributes = all_quest_data['attributes']

        assert_payload_field_type(self, attributes, 'quests', list)

        quest = attributes['quests'][0]

        assert_payload_field_type(self, quest, 'quest_id_2', dict)

        quest_data = quest['quest_id_2']

        assert_payload_field_type_value(self, quest_data, 'encounter_req', int, self.quest_2.encounter_req)
        assert_payload_field_type_value(self, quest_data, 'id', int, self.quest_2.id)
        assert_payload_field_type_value(self, quest_data, 'name', str, self.quest_2.name)
        assert_payload_field_type_value(self, quest_data, 'progress', int, self.user_quest_2.progress)
        assert_payload_field_type_value(self, quest_data, 'type', str, self.quest_2.type)
        assert_payload_field_type_value(self, quest_data, 'xp', int, self.quest_2.xp)
        assert_payload_field_type_value(self, quest_data, 'level', int, self.quest_2.level)

    def test_happy_path_get_quests_for_user_false(self):
        response = self.client.get(f'/api/v1/users/{self.user_1.id}/quests?completion_status=false', content_type='application/json')

        self.assertEqual(200, response.status_code)

        data = json.loads(response.data.decode('utf-8'))

        assert_payload_field_type(self, data, 'data', dict)

        all_quest_data = data['data']

        assert_payload_field_type_value(self, all_quest_data, 'id', str, 'Null')
        assert_payload_field_type_value(self, all_quest_data, 'type', str, 'quests')

        attributes = all_quest_data['attributes']

        assert_payload_field_type(self, attributes, 'quests', list)

        quest = attributes['quests'][0]

        assert_payload_field_type(self, quest, 'quest_id_1', dict)

        quest_data = quest['quest_id_1']

        assert_payload_field_type_value(self, quest_data, 'encounter_req', int, self.quest_1.encounter_req)
        assert_payload_field_type_value(self, quest_data, 'id', int, self.quest_1.id)
        assert_payload_field_type_value(self, quest_data, 'name', str, self.quest_1.name)
        assert_payload_field_type_value(self, quest_data, 'progress', int, self.user_quest_1.progress)
        assert_payload_field_type_value(self, quest_data, 'type', str, self.quest_1.type)
        assert_payload_field_type_value(self, quest_data, 'xp', int, self.quest_1.xp)
        assert_payload_field_type_value(self, quest_data, 'level', int, self.quest_1.level)

    def test_sad_path_get_quests_for_user_no_params(self):
        response = self.client.get(f"/api/v1/users/{self.user_1.id}/quests", content_type='application/json')

        self.assertEqual(500, response.status_code)

        # Come back and add in error messaging later

    def test_for_user_without_user_quests(self):
        new_user = User(username='Billy', email="billy@example.com", xp=0)
        db.session.add(new_user)
        db.session.commit()

        user_quests = new_user.user_quests.all().__len__()

        self.assertEqual(0, user_quests)

        response = self.client.get(f'/api/v1/users/{new_user.id}/quests?completion_status=false', content_type='application/json')

        user_quests = new_user.user_quests.all().__len__()

        self.assertEqual(3, user_quests)
