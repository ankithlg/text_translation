import unittest
from app import app

class TestTranslationApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Translate', response.data)

    def test_translation(self):
        response = self.app.post('/', data={
            'input_text': 'hello',
            'src_lang': 'en',
            'dest_lang': 'fr'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'bonjour', response.data.lower())  # adjust for real translation output

if __name__ == '__main__':
    unittest.main()

