import json
import unittest
from unittest.mock import patch
from copy import deepcopy

from api import create_app, db
from api.database.models.users import User
from tests import db_drop_everything, assert_payload_field_type_value, \
    assert_payload_field_type


class GetAllUsersTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

        self.user_1 = User(username='zzz 1', email='e1', xp=0)
        self.user_1.insert()

        self.user_2 = User(username='aaa 2', email='e2', xp=0)
        self.user_2.insert()

    def tearDown(self):
        db.session.remove()
        db_drop_everything(db)
        self.app_context.pop()

    def test_happypath_get_all_users(self):
        response = self.client.get(
                    '/api/v1/users',
                    content_type='application/json'
                )
        self.assertEqual(200, response.status_code)

        data = json.loads(response.data.decode('utf-8'))

        assert_payload_field_type_value(self, data, 'success', bool, True)

        assert_payload_field_type(self, data, 'data', dict)
        users_data = data['data']

        assert_payload_field_type_value(
            self, users_data, 'type', str, 'users'
        )

        attributes = users_data['attributes']

        assert_payload_field_type_value(
        self, attributes[0], 'id', int, self.user_1.id
        )
        assert_payload_field_type_value(
        self, attributes[1], 'id', int, self.user_2.id
        )

        assert_payload_field_type_value(
            self, attributes[0], 'username', str, self.user_1.username
        )
        assert_payload_field_type_value(
            self, attributes[1], 'username', str, self.user_2.username
        )

        assert_payload_field_type_value(
            self, attributes[0], 'email', str, self.user_1.email
        )

        assert_payload_field_type_value(
            self, attributes[1], 'email', str, self.user_2.email
        )

        assert_payload_field_type_value(
            self, attributes[0], 'xp', int, self.user_1.xp
        )

        assert_payload_field_type_value(
            self, attributes[1], 'xp', int, self.user_2.xp
        )

    def test_endpoint_sadpath_bad_email_user(self):
        response = self.client.get(
                '/api/v1',
                content_type='application/json'
            )
        self.assertEqual(404, response.status_code)

        data = json.loads(response.data.decode('utf-8'))
        assert_payload_field_type_value(self, data, 'error', int, 404)
        assert_payload_field_type_value(self, data, 'success', bool, False)
        assert_payload_field_type_value(
            self, data, 'message', str, 'resource not found'
        )
