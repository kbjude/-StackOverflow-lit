import unittest
from flask import Flask
from api.app import my_app
import json
    
class TestSignup(unittest.TestCase):

    def setUp(self):
        self.app = my_app
        self.client = self.app.test_client

    def tearDown(self):
        pass

    def test_missing_username(self):
        '''Test for a missing username'''
        result = self.client().post('/signup',data=json.dumps({'password':'123455','confirm':'123455'}), content_type="application/json")
        self.assertEqual(result.status_code, 400)
        self.assertIn('You did not specify a username',str(result.data))

    def test_missing_password(self):
        result = self.client().post('/signup',data=json.dumps({'username':'jude', 'confirm':'12345'}), content_type="application/json")
        self.assertEqual(result.status_code, 400)
        self.assertIn('Missing password', str(result.data))
    
    def test_missing_confirm(self):
        result = self.client().post('/signup',data=json.dumps({'username':'jude', 'password':'12345'}), content_type="application/json")
        self.assertEqual(result.status_code, 400)
        self.assertIn('Type to confirm the password', str(result.data))
    
class TestSignIn(unittest.TestCase):

    def setUp(self):
        self.app = my_app
        self.client = self.app.test_client

    def tearDown(self):
        pass

    def test_missing_username(self):
        """Testing for a missing username at login"""
        result = self.client().post('/signin',data=json.dumps({'password':'christlord'}), content_type="application/json")
        self.assertEqual(result.status_code, 400)
        self.assertIn('Missing username', str(result.data))
    
    def test_missing_password(self):
        """Testing for missing password at login"""
        result = self.client().post('/signin',data=json.dumps({'username':'jude'}), content_type="application/json")
        self.assertEqual(result.status_code, 400)
        self.assertIn('Missing password', str(result.data))
