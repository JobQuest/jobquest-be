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

# def _format_quests(quests):
#     map(json.dumps, quests)

def _user_quest_payload(quests):
    return {
        'data': {
            'id': 'Null',
            'type': 'quests',
            'attributes': {
                 "quests":
                 map(json.loads(quests))
            }
        }
    }

class UserQuestsResource(Resource):

    def get(self, *args, **kwargs):
        user_id = request.view_args['user_id']
        completion_status = request.args['completion_status']
        quests = []

        try:
            user = User.query.filter_by(id=user_id).one()
            user_quests = user.user_quests.filter_by(completion_status=completion_status).all()
            for user_quest in user_quests:
                quest_id = user_quest.quest_id
                quests.append(Quest.query.filter_by(id=quest_id).one())

        except NoResultFound:
            return abort(404)

        user_quest_payload = _user_quest_payload(quests)
        user_quest_payload['success'] = True
        return user_quest_payload, 200
