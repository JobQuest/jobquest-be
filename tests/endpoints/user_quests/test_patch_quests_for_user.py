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

class PatchQuestsTest(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()
		self.client = self.app.test_client()

		self.user_1 = User(username='George', email="george@example.com", xp=0)
		self.user_1.insert()
		self.user_2 = User(username='Carson', email="carson@example.com", xp=0)
		self.user_2.insert()
		self.quest_1 = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active')
		self.quest_2 = Quest(name="Make'a da biscuit!", xp=10, level=2, encounter_req=1, type='active')
		self.quest_3 = Quest(name="Make'a da nuggets!", xp=15, level=3, encounter_req=5, type='active')
		self.quest_4 = Quest(name="Make'a da wings!", xp=15, level=3, encounter_req=5, type='passive')
		self.quest_1.insert()
		self.quest_2.insert()
		self.quest_3.insert()
		self.quest_4.insert()

		self.user_quest_1 = UserQuest(quest_id=self.quest_1.id, user_id=self.user_1.id, progress=1, completion_status=False)
		self.user_quest_2 = UserQuest(quest_id=self.quest_2.id, user_id=self.user_1.id, progress=1, completion_status=False)
		self.user_quest_3 = UserQuest(quest_id=self.quest_4.id, user_id=self.user_1.id, progress=5, completion_status=False)
		self.user_quest_4 = UserQuest(quest_id=self.quest_2.id, user_id=self.user_2.id, progress=1, completion_status=False)

		self.user_quest_1.insert()
		self.user_quest_2.insert()
		self.user_quest_3.insert()
		self.user_quest_4.insert()

		self.payload = {
						'quest_id': int(self.quest_1.id),
						'progress': int(2)
		}
		self.payload2 = {
						'quest_id': int(self.quest_2.id),
						'progress': int(2)
		}
		self.payload3 = {
						'quest_id': int(self.quest_4.id),
						'progress': int(6)
		}
		self.payload4 = {
						'quest_id': int(self.quest_2.id),
						'progress': int(1)
		}

	def tearDown(self):
		db.session.remove()
		db_drop_everything(db)
		self.app_context.pop()

	def test_happy_path_user_quest_progress_can_be_patched(self):
		payload = deepcopy(self.payload)
		response = self.client.patch(f'/api/v1/users/{self.user_1.id}/quests', json=payload, content_type='application/json')

		self.assertEqual(201, response.status_code)
		data = json.loads(response.data.decode('utf-8'))
		assert_payload_field_type(self, data, 'data', dict)

		all_user_quest_data = data['data']

		assert_payload_field_type_value(self, all_user_quest_data, 'id', int, self.user_quest_1.id)
		assert_payload_field_type_value(self, all_user_quest_data, 'type', str, 'user_quests')
		assert_payload_field_type(self, all_user_quest_data, 'attributes', dict)

		attributes = all_user_quest_data['attributes']

		assert_payload_field_type_value(self, attributes, 'response', str, 'successful')
		assert_payload_field_type_value(self, attributes, 'progress', int, int(payload['progress']))
		assert_payload_field_type_value(self, attributes, 'completion_status', bool, False)

	def test_happy_path_progress_change_can_update_completion_status(self):
		payload2 = deepcopy(self.payload2)
		response = self.client.patch(f'/api/v1/users/{self.user_1.id}/quests', json=payload2, content_type='application/json')

		self.assertEqual(201, response.status_code)
		data = json.loads(response.data.decode('utf-8'))
		assert_payload_field_type(self, data, 'data', dict)

		all_user_quest_data = data['data']

		assert_payload_field_type_value(self, all_user_quest_data, 'id', int, self.user_quest_2.id)
		assert_payload_field_type_value(self, all_user_quest_data, 'type', str, 'user_quests')
		assert_payload_field_type(self, all_user_quest_data, 'attributes', dict)

		attributes = all_user_quest_data['attributes']

		assert_payload_field_type_value(self, attributes, 'response', str, 'successful')
		assert_payload_field_type_value(self, attributes, 'progress', int, int(payload2['progress']))
		assert_payload_field_type_value(self, attributes, 'completion_status', bool, True)

	def test_sad_path_get_quests_for_user_no_params(self):
		response = self.client.patch(f"/api/v1/users/{self.user_1.id}/quests", content_type='application/json')

		self.assertEqual(400, response.status_code)
		# Come back and add in error messaging later

	def test_user_gains_xp_when_they_complete_quests(self):
		self.assertEqual(0, self.user_1.xp)
		payload2 = deepcopy(self.payload2)

		response = self.client.patch(f'/api/v1/users/{self.user_1.id}/quests', json=payload2, content_type='application/json')

		self.assertEqual(10, self.user_1.xp)

	def test_user_gets_new_quest_when_they_complete_quests(self):
		user_quests_total = self.user_1.user_quests.all().__len__()
		self.assertEqual(3, user_quests_total)
		payload2 = deepcopy(self.payload2)

		response = self.client.patch(f'/api/v1/users/{self.user_1.id}/quests', json=payload2, content_type='application/json')

		user_quests_total = self.user_1.user_quests.all().__len__()
		self.assertEqual(4, user_quests_total)

		new_user_quest = self.user_1.user_quests.all()[-1]
		self.assertEqual(3, new_user_quest.quest_id)

		quest = Quest.query.filter_by(id=new_user_quest.quest_id).one()
		self.assertEqual(self.quest_3.level, quest.level)
		self.assertEqual(self.quest_3.name, quest.name)
		self.assertEqual(self.quest_3.type, quest.type)

	def test_when_user_completes_all_levels_of_quest_path(self):
		payload3 = deepcopy(self.payload3)
		response = self.client.patch(f'/api/v1/users/{self.user_1.id}/quests', json=payload3, content_type='application/json')

		user_quests_total = self.user_1.user_quests.all().__len__()
		self.assertEqual(3, user_quests_total)

		user_xp = self.user_1.xp
		self.assertEqual(15, user_xp)

		user_quest_status = self.user_quest_3.completion_status
		self.assertEqual(True, user_quest_status)

	def test_sad_path_progress_doesnt_change(self):
		payload4 = deepcopy(self.payload4)
		response = self.client.patch(f'/api/v1/users/{self.user_2.id}/quests', json=payload4, content_type='application/json')

		self.assertEqual(404, response.status_code)

	def test_sad_path_user_does_not_exist(self):
		payload4 = deepcopy(self.payload4)
		response = self.client.patch(f'/api/v1/users/12/quests', json=payload4, content_type='application/json')
		
		self.assertEqual(404, response.status_code)
