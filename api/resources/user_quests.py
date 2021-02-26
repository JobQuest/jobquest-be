import datetime
import json
from flask import jsonify

import bleach
from flask import request
from flask_restful import Resource, abort, reqparse, fields, marshal_with
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Quest
from api.database.models import User
from api.database.models import UserQuest

def _user_quest_payload(quests):
    quest_objects = {}
    for progress, quest in quests.items():
        quest_objects[f"quest_id_{quest.id}"] = {
            'id': quest.id,
            'type': quest.type,
            'name': quest.name,
            'xp': quest.xp,
            'encounter_req': quest.encounter_req,
            'level': quest.level,
            'progress': int(progress)
        }

    return {
        'data': {
            'id': 'Null',
            'type': 'quests',
            'attributes': {
                 "quests": [quest_objects]
            }
        }
    }

def _patched_user_quest_payload(user_quest):
    return {
        'data': {
            'id': user_quest.id,
            'type': 'user_quests',
            'attributes': {
                 'response': 'successful',
                 'progress': user_quest.progress,
                 'completion_status': user_quest.completion_status
            }
        }
    }

class UserQuestsResource(Resource):

    def get(self, *args, **kwargs):
        user_id = request.view_args['user_id']
        quests = {}

        try:
            completion_status = request.args['completion_status']
            user = User.query.filter_by(id=user_id).one()
            user_quests = user.user_quests.filter_by(completion_status=completion_status).all()
            for user_quest in user_quests:
                progress = user_quest.progress
                quest_id = user_quest.quest_id
                quests[str(progress)] = Quest.query.filter_by(id=quest_id).one()

        except NoResultFound:
            return abort(404)

        except BadRequestKeyError:
            return abort()

        user_quest_payload = _user_quest_payload(quests)
        return user_quest_payload, 200

    def patch(self, *args, **kwargs):
        user_id = request.view_args['user_id']
        data = request.get_json()

        try:
            user = User.query.filter_by(id=user_id).one()
            user_quest = user.user_quests.filter_by(quest_id=data['quest_id']).one()
            quest = Quest.query.filter_by(id=user_quest.quest_id).one()
            user_quest.progress = data['progress']
            db.session.add(user_quest)
            db.session.commit()
            if user_quest.progress > quest.encounter_req:
                user_quest.completion_status = True
                db.session.add(user_quest)
                db.session.commit()


        except NoResultFound:
            return abort(404)

        patched_user_quest_payload = _patched_user_quest_payload(user_quest)
        return patched_user_quest_payload, 201
