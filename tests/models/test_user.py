import unittest
from sqlalchemy.exc import IntegrityError

from api import create_app, db
from api.database.models.users import User

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_model(self):
        user = User(username='ian', email='ian.douglas@iandouglas.com', xp=0)
        user.insert()

        self.assertIsInstance(user, User)
        self.assertIsNotNone(user.id)
        self.assertEqual('ian', user.username)
        self.assertEqual('ian.douglas@iandouglas.com', user.email)

    def test_user_model_with_forced_id(self):
        user = User(username='ian',
                    email='ian.douglas@iandouglas.com',
                    xp=0,
                    user_id=1)
        user.insert()

        self.assertIsInstance(user, User)
        self.assertIsNotNone(user.id)
        self.assertEqual(1, user.id)
        self.assertEqual('ian', user.username)
        self.assertEqual('ian.douglas@iandouglas.com', user.email)

    def test_user_model_trimmed_username(self):
        user = User(username=' ian ', email='ian.douglas@iandouglas.com', xp=0)
        user.insert()

        self.assertEqual('ian', user.username)

    def test_user_model_trimmed_email(self):
        user = User(username='ian', email=' ian.douglas@iandouglas.com ', xp=0)
        user.insert()

        self.assertEqual('ian.douglas@iandouglas.com', user.email)

    def test_user_model_username_does_not_have_to_be_unique(self):
        user = User(username='ian', email='ian.douglas@iandouglas.com', xp=0)
        user.insert()

        try:
            user = User(username='ian', email='ian.douglas+2@iandouglas.com', xp=0)
            user.insert()
        except IntegrityError:
            self.assertTrue(False)
        else:
            self.assertTrue(True)


    def test_user_model_blank_username(self):
        try:
            user = User(username='', email='ian.douglas@iandouglas.com', xp=0)
            user.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            # we should not end up in here
            self.assertTrue(False)  # pragma: no cover

    def test_user_model_missing_username(self):
        try:
            user = User(username=None, email='ian.douglas@iandouglas.com', xp=0)
            user.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            # we should not end up in here
            self.assertTrue(False)  # pragma: no cover

    def test_user_model_unique_email(self):
        user = User(username='ian', email='ian.douglas@iandouglas.com', xp=0)
        user.insert()

        try:
            user = User(username='ian2', email='ian.douglas@iandouglas.com', xp=0)
            user.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)  # pragma: no cover

    def test_user_model_blank_email(self):
        try:
            user = User(username='ian', email='', xp=0)
            user.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)  # pragma: no cover

    def test_user_model_missing_email(self):
        try:
            user = User(username='ian', email=None, xp=0)
            user.insert()
        except IntegrityError:
            self.assertTrue(True)
        else:
            # we should not end up in here
            self.assertTrue(False)  # pragma: no cover

    def test_user_can_update_attributes(self):
        user = User(username='ian', email='ian.douglas@iandouglas.com', xp=0)
        user.insert()

        self.assertEqual('ian', user.username)
        self.assertEqual('ian.douglas@iandouglas.com', user.email)
        self.assertEqual(0, user.xp)

        user = User(username='ian2', email='ian.douglas@iandouglas.com', xp=100)
        user.update()

        self.assertEqual('ian2', user.username)
        self.assertEqual('ian.douglas@iandouglas.com', user.email)
        self.assertEqual(100, user.xp)

    def test_user_can_be_deleted(self):
        user = User(username='ian', email='ian.douglas@iandouglas.com', xp=0)
        user.insert()

        user_2 = User(username='cj', email='carson@iandouglas.com', xp=0)
        user_2.insert()

        self.assertEqual(User.query.count(), 2)

        user.delete()
        self.assertEqual(User.query.count(), 1)
