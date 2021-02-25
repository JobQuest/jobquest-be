import json
import unittest
from unittest.mock import patch
from copy import deepcopy
from api import create_app, db
from api.database.models import UserQuest, User, Quest
from tests import db_drop_everything, assert_payload_field_type_value, \
		assert_payload_field_type

class PatchQuestsTest(unittest.TestCase):
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
				self.user_quest_2 = UserQuest(quest_id=self.quest_2.id, user_id=self.user_1.id, progress=3, completion_status=False)
				db.session.add(self.user_quest_1)
				db.session.commit()
				db.session.add(self.user_quest_2)
				db.session.commit()
				self.payload = {
								'quest_id': str(self.quest_1.id), 
								'progress': str(2)
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