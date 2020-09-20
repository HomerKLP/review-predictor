# Vendor
from rest_framework.test import APITestCase
from django.urls import reverse


class ReviewTest(APITestCase):
    """Тест отзывов"""
    url = None

    def __init__(self, method_name='runTest'):
        self.url = reverse('reviews')
        super().__init__(method_name)

    def test_create_review(self):
        payload = {'text': 'text'}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, 201)

    def test_list_review(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
