# This will be used when we have the capability to create a new user with every
# `POST '/api/v1/users'` request. This is set up to use when that Auth0 is up and running
# When you use this test, the tests in `test_get_user_by_email.py` will no longer be needed

# import json
# import unittest
# from unittest.mock import patch
# from copy import deepcopy
#
# from api import create_app, db
# from api.database.models.users import User
# from tests import db_drop_everything, assert_payload_field_type_value, \
#     assert_payload_field_type
#
# class PostUserTest(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app('testing')
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         db.create_all()
#         self.client = self.app.test_client()
#
#     def tearDown(self):
#         db.session.remove()
#         db_drop_everything(db)
#         self.app_context.pop()
#
#     def test_happypath_a_user_can_be_created_in_database(self):
#         payload = {
#                 'username': 'Test',
#                 'email': 'test@example.com'
#         }
#
#         response = self.client.post(
#                     '/api/v1/users', json=payload,
#                     content_type='application/json'
#                 )
#
#         self.assertEqual(200, response.status_code)
#
#         data = json.loads(response.data.decode('utf-8'))
#
#         assert_payload_field_type_value(self, data, 'success', bool, True)
#
#         assert_payload_field_type(self, data, 'data', dict)
#
#         user_data = data['data']
#
#         assert_payload_field_type_value(
#             self, user_data, 'id', int, 1
#         )
#
#         assert_payload_field_type_value(
#             self, user_data, 'type', str, 'users'
#         )
#
#         attributes = user_data['attributes']
#         # breakpoint()
#         assert_payload_field_type_value(
#             self, attributes, 'username', str, payload['username']
#         )
#
#         assert_payload_field_type_value(
#             self, attributes, 'email', str, payload['email']
#         )
#
#         assert_payload_field_type_value(
#             self, attributes, 'xp', int, 0
#         )
#
#     def test_endpoint_sadpath_bad_email_user(self):
#         user_1 = User(username='Test', email='user@example.com', xp=0)
#         user_1.insert()
#
#         payload = {
#                 'username': 'Test',
#                 'email': 'user@example.com'
#         }
#
#         response = self.client.post(
#                 '/api/v1/users', json=payload,
#                 content_type='application/json'
#             )
#
#         self.assertEqual(500, response.status_code)
#
#     def test_endpoint_sadpath_username_is_same_unique_email(self):
#         user_1 = User(username='Test', email='user@example.com', xp=0)
#         user_1.insert()
#
#         payload = {
#                 'username': 'Test',
#                 'email': 'test@example.com'
#         }
#
#         response = self.client.post(
#                 '/api/v1/users', json=payload,
#                 content_type='application/json'
#             )
#
#         self.assertEqual(200, response.status_code)
