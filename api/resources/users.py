import datetime
import json
from flask import jsonify

import bleach
from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models.users import User

def _user_payload(user):
    return {
        'data': {
            'id': user.id,
            'type': 'users',
            'attributes': {
                'email': user.email,
                'username': user.username,
                'xp': user.xp
            }
        }
    }

def _serial_users(users):
    serializable_users = []

    for user in users:
        serializable_users.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'xp': user.xp
        })

    return serializable_users

def _users_payload(users):
    return {
        'data': {
            'id': None,
            'type': 'users',
            'attributes': _serial_users(users)
        }
    }

class UserResource(Resource):
    """
    this Resource file is for our /users endpoints which don't require
    a resource ID in the URI path
    """

    def post(self, *args, **kwargs):
        data = request.get_json()
        user_email = data['email']
        user_name = ""

        if 'username' in data.keys():
            user_name = data['username']
        else:
            user_name = data['email'].split('@')[0]

        user = User.query.filter_by(email=user_email).all()

        if user != []:
            user = user[0]
            user_payload = _user_payload(user)
            user_payload['success'] = True
            user_payload['user_action'] = 'retrieved'
            return user_payload, 200
        else:
            new_user = User(username= user_name, email=user_email, xp=0)
            new_user.insert()
            user_payload = _user_payload(new_user)
            user_payload['success'] = True
            user_payload['user_action'] = 'created'
            return user_payload, 201

    def get(self):
        users = User.query.all()

        users_payload = _users_payload(users)
        users_payload['success'] = True
        return users_payload, 200
