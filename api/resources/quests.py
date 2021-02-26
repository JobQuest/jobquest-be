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
from api.database.models import Encounter
from api.database.models import Action

def _quest_payload(quest):

class QuestResource(Resource):
    def get(self, *args, **kwargs):
        quest_id = request.view_args['id']
        quest = {}

        try:
            progress = request.args['progress']
            quest = Quest.query.filter_by(id=quest_id).one()
