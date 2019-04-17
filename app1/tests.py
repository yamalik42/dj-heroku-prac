from django.test import TestCase
from django.test import Client
import json

# Create your tests here.
class AppOneTestCase(TestCase):
    def test_message_response(self):
        c = Client()
        body = json.dumps({
            "content": "Some test text.",
            "filename": "for_test_case"
        })
        res1 = c.post('/app1/', body, content_type='application/json')
        res2 = c.get('/app1/?filename=abc.txt')
        self.assertEqual(res1.content, b'created file')
        self.assertEqual(res2.content, b'some text to read with the app')