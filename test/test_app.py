import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_no_file(self):
        response = self.client.post('/analyze')
        self.assertEqual(response.status_code, 400)

    def test_upload(self):
        with open('sample_passport.jpg', 'rb') as f:
            data = {'file': f}
            response = self.client.post('/analyze', data=data)
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()