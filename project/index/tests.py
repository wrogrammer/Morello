from django.test import TestCase


class IndexViewTestCase(TestCase):
    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
