import json
import unittest
from unittest.mock import patch
from copy import deepcopy

from api import create_app, db
from api.database.models.users import User
from tests import db_drop_everything, assert_payload_field_type_value, \
    assert_payload_field_type


class GetUserTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

        self.user_1 = User(username='zzz 1', email='e1', xp=0)
        self.user_1.insert()

        self.payload = {
                'email': 'e1'
        }

    def tearDown(self):
        db.session.remove()
        db_drop_everything(db)
        self.app_context.pop()

    def test_happypath_get_a_user_by_email(self):
        payload = deepcopy(self.payload)
        response = self.client.post(
                    '/api/v1/users', json=payload,
                    content_type='application/json'
                )
        self.assertEqual(200, response.status_code)

        data = json.loads(response.data.decode('utf-8'))

        assert_payload_field_type_value(self, data, 'success', bool, True)

        assert_payload_field_type(self, data, 'data', dict)

        user_data = data['data']

        assert_payload_field_type_value(
            self, user_data, 'id', int, self.user_1.id
        )

        assert_payload_field_type_value(
            self, user_data, 'type', str, 'users'
        )

        attributes = user_data['attributes']

        assert_payload_field_type_value(
            self, attributes, 'username', str, self.user_1.username
        )

        assert_payload_field_type_value(
            self, attributes, 'email', str, self.user_1.email
        )

        assert_payload_field_type_value(
            self, attributes, 'xp', int, self.user_1.xp
        )

    def test_endpoint_will_return_a(self):
        payload = {'email': 'bademail@example.com'}
        response = self.client.post(
                '/api/v1/users', json=payload,
                content_type='application/json'
            )
        self.assertEqual(201, response.status_code)

        data = json.loads(response.data.decode('utf-8'))
        assert_payload_field_type_value(self, data, 'user_action', str, 'created')
