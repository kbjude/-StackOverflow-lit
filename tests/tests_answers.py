import unittest
from flask import Flask
from api.app import my_app
import json

class Answers(unittest.TestCase):
    def setUp(self):
        self.app = my_app
        self.client = self.app.test_client

    def tearDown(self):
            pass
    
    def test_missing_id(self):
        result = self.client().post('/answers', data=json.dumps({'answer':'answer'}))
        self.assertEqual(result.status_code, 400)
        self.assertIn('Missing answer',str(result.data))