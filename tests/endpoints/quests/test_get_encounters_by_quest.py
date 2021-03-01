import json
import unittest
from unittest.mock import patch
from copy import deepcopy
from api import create_app, db
from api.database.models.users import User
from api.database.models.quests import Quest
from api.database.models.user_quests import UserQuest
from api.database.models.encounters import Encounter
from api.database.models.actions import Action
from tests import db_drop_everything, assert_payload_field_type_value, \
    assert_payload_field_type

class GetEncountersByQuest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

        self.user_1 = User(username='Steve', email="steve@example.com", xp=1000000000)
        self.user_1.insert()
        self.quest_1 = Quest(name="Make'a da pancake!", xp=5, level=1, encounter_req=3, type='active')
        self.quest_2 = Quest(name="Make'a da biscuit!", xp=10, level=2, encounter_req=3, type='active')
        self.quest_1.insert()
        self.quest_2.insert()

        self.user_quest_1 = UserQuest(quest_id=self.quest_1.id, user_id=self.user_1.id, progress=1, completion_status=False)
        self.user_quest_2 = UserQuest(quest_id=self.quest_2.id, user_id=self.user_1.id, progress=1, completion_status=True)
        self.user_quest_1.insert()
        self.user_quest_2.insert()

        self.encounter_1 = Encounter(monster_image='https://images.huffingtonpost.com/2015-02-05-trollersTroll-thumb.jpg', quest_id=self.quest_1.id, progress=1)
        self.encounter_1.insert()

        self.encounter_2 = Encounter(monster_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdIfSV09BWeNuPejZM4txwTFJJKikYV_WMLg&usqp=CAU', quest_id=self.quest_1.id, progress=2)
        self.encounter_2.insert()

        self.action_1 = Action(encounter_id=self.encounter_1.id,  description='Send a message to a recruiter')
        self.action_2 = Action(encounter_id=self.encounter_1.id, description='Apply to a Job')
        self.action_3 = Action(encounter_id=self.encounter_2.id, description='Schedule a coffee meetup with a target Company')

        self.action_1.insert()
        self.action_2.insert()
        self.action_3.insert()

    def tearDown(self):
        db.session.remove()
        db_drop_everything(db)
        self.app_context.pop()

    def test_happy_path_get_encounters_for_quest_by_progress(self):
        response = self.client.get(f'/api/v1/quests/{self.quest_1.id}/encounters?progress=2', content_type='application/json')
        self.assertEqual(200, response.status_code)
        data = json.loads(response.data.decode('utf-8'))
        assert_payload_field_type(self, data, 'data', dict)
        encounter_data = data['data']
        assert_payload_field_type_value(self, encounter_data, 'id', int, self.encounter_2.id)
        assert_payload_field_type_value(self, encounter_data, 'type', str, 'encounters')
        attributes = encounter_data['attributes']
        assert_payload_field_type(self, encounter_data, 'attributes', dict)
        assert_payload_field_type_value(self, attributes, 'progress', int, self.encounter_2.progress)
        assert_payload_field_type_value(self, attributes, 'monster_image', str, self.encounter_2.monster_image)
        assert_payload_field_type(self, attributes, 'actions', list)
        actions = attributes['actions']
        assert_payload_field_type_value(self, actions[0], 'id', int, self.action_3.id)
        assert_payload_field_type_value(self, actions[0], 'description', str, self.action_3.description)

    def test_sad_path_get_encounters_for_quest_when_no_progress_given(self):
        response = self.client.get(f'/api/v1/quests/{self.quest_1.id}/encounters?progress=', content_type='application/json')
        self.assertEqual(500, response.status_code)

    def test_sad_path_get_encounters_for_quest_when_wrong_progress_given(self):
        response = self.client.get(
            f'/api/v1/quests/{self.quest_1.id}/encounters?progress=896', content_type='application/json')
        self.assertEqual(404, response.status_code)
