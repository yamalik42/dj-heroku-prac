from django.test import TestCase
from django.test import Client

# Create your tests here.
class AppTwoTestCase(TestCase):
    def test_message_response(self):
        c = Client()
        res1 = c.get('/app2/2')
        res2 = c.get('/app2/7')
        res3 = c.get('/app2/18')
        res4 = c.get('/app2/20')
        self.assertEqual(res1.content, b'Go To Bed')
        self.assertEqual(res2.content, b'Good Morning')
        self.assertEqual(res3.content, b'Good Afternoon')
        self.assertEqual(res4.content, b'Not the correct greeting')