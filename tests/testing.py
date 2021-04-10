import os
import sys
import unittest
sys.path.append("../")
from project import app


class UnitTests(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('PROJECT_SQLALCHEMY_DATABASE')
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def test_index_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.app.post(
            '/register',
            data=dict(email="asdas@gmail.com", password="***REMOVED_PASSWORD***", confirm="***REMOVED_PASSWORD***", phone="8282828384"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_login_user(self):
        response = self.app.post(
            '/login',
            data=dict(email="patel.farhaaan@gmail.com", password="***REMOVED_PASSWORD***"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
