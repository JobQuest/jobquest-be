import json
import unittest
from unittest.mock import patch
from copy import deepcopy
from api import create_app, db
from api.database.models import UserQuest, User, Quest
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
        db.session.add(self.quest_1)
        db.session.commit()
        db.session.add(self.quest_2)
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

    def test_happy_path_get_quests_for_user(self):
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
