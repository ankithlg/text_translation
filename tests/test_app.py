import unittest
from app import app

class TranslationAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_translation_post(self):
        response = self.app.post('/translate', data=dict(
            text="hello",
            target_lang="fr"
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'bonjour', response.data)  # Adjust depending on actual result

if __name__ == '__main__':
    unittest.main()
