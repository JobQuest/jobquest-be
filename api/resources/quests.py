import datetime
import json
from flask import jsonify

import bleach
from flask import request
from flask_restful import Resource, abort, reqparse, fields, marshal_with
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models.quests import Quest
from api.database.models.users import User
from api.database.models.user_quests import UserQuest
from api.database.models.encounters import Encounter
from api.database.models.actions import Action

def _quest_encounters_payload(encounter):
    return {
        'data': {
            'id': encounter.id,
            'type': 'encounters',
            'attributes': {
                'progress': encounter.progress,
                'monster_image': encounter.monster_image,
                'actions': _serial_actions(encounter.actions)
            }
        }
    }

def _serial_actions(actions):
    serial_actions = []

    for action in actions:
        serial_actions.append({
            'id': action.id,
            'description': action.description
        })

    return serial_actions

class QuestResource(Resource):
    def get(self, *args, **kwargs):
        quest_id = request.view_args['quest_id']
        quest = {}
        try:
            progress = request.args['progress']
            quest = Quest.query.filter_by(id=quest_id).one()
            encounter = quest.encounters.filter_by(progress=progress).one()

        except NoResultFound:
            return abort(404)

        quest_encounters_payload = _quest_encounters_payload(encounter)
        return quest_encounters_payload, 200
