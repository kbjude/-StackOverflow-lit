import unittest
from flask import Flask
from api.app import my_app
import json   

class Question(unittest.TestCase):

    def setUp(self):
        self.app = my_app
        self.client = self.app.test_client

    def tearDown(self):
        pass

    def test_missing_content(self):
        result = self.client().post('/questions',data=json.dumps({'category':'test'}), content_type="application/json")
        self.assertEqual(result.status_code, 400)
        self.assertIn('Provide a question',str(result.data))

    def test_missing_category(self):
        result = self.client().post('/questions',data=json.dumps({'content':'test'}), content_type="application/json")
        self.assertEqual(result.status_code, 400)
        self.assertIn('Provide the right category',str(result.data))