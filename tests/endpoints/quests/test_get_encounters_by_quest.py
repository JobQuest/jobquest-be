import json
import unittest
from unittest.mock import patch
from copy import deepcopy
from api import create_app, db
from api.database.models import UserQuest, User, Quest
from tests import db_drop_everything, assert_payload_field_type_value, \
    assert_payload_field_type

class GetEncountersByQuest(unittest.TestCase):
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
        self.encounter_1 = Encounter(monster_image='https://images.huffingtonpost.com/2015-02-05-trollersTroll-thumb.jpg', quest_id=self.quest_1.id, progress=1)
        db.session.add(self.encounter_1)
        db.session.commit()
        self.encounter_2 = Encounter(monster_image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdIfSV09BWeNuPejZM4txwTFJJKikYV_WMLg&usqp=CAU', quest_id=self.quest_1.id, progress=2)
        db.session.add(self.encounter_2)
        db.session.commit()
        self.action_1 = Action(encounter_id=self.encounter_1.id,  description='Send a message to a recruiter')
        db.session.add(self.action_1)
        db.session.commit()
        self.action_2 = Action(encounter_id=self.encounter_1.id, description='Apply to a Job')
        db.session.add(self.action_2)
        db.session.commit()
        self.action_3 = Action(encounter_id=self.encounter_2.id, description='Schedule a coffee meetup with a target Company')
        db.session.add(self.action_3)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db_drop_everything(db)
        self.app_context.pop()

    def test_happy_path_get_encounters_for_quest_by_progress(self):
        response = self.client.get(f'/api/v1/quests/{self.quest_1.id}/encounters?progress=2', content_type='application/json')
        breakpoint()
