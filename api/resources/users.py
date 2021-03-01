import datetime
import json
from flask import jsonify

import bleach
from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models.users import User


def _validate_field(data, field, proceed, errors, missing_okay=False):
    if field in data:
        # sanitize the user input here
        data[field] = bleach.clean(data[field].strip())
        if len(data[field]) == 0:
            proceed = False
            errors.append(f"required '{field}' parameter is blank")
    if not missing_okay and field not in data:
        proceed = False
        errors.append(f"required '{field}' parameter is missing")
        data[field] = ''

    return proceed, data[field], errors

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

        # lines 74 to 78 will be used when Auth0 is enabled

        # breakpoint()
        # if data['username']:
        #     user_name = data['username']
        # else:
        #     user_name = data['email'].split('@')[0]
        if data['username'].raiseError:
            user_name = data['email'].split('@')[0]
        else:
            user_name = data['username']

        # new_user = User(username= username, email=user_email, xp=0)
        # db.session.add(new_user)
        # db.session.commit()
        user = User.query.filter_by(email=user_email).all()
        try:
            if user != []:
                user = user.one()
                user_payload = _user_payload(user)
                user_payload['success'] = True
                return user_payload, 200
            else:
                new_user = User(username= user_name, email=user_email, xp=0)
                breakpoint()
                db.session.add(new_user)
                db.session.commit()
                user_payload = _user_payload(new_user)
                user_payload['success'] = True
                return user_payload, 201

        except NoResultFound:
            return abort(404)

        # user_payload = _user_payload(user)
        # user_payload['success'] = True
        # # return user_payload, 201
        # return user_payload, 200

    def get(self):
        try:
            users = User.query.all()
        except NoResultFound:
            return abort(404)

        users_payload = _users_payload(users)
        users_payload['success'] = True
        return users_payload, 200
