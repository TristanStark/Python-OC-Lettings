from django.test import TestCase
from django.urls import reverse


class HomePageViewTest(TestCase):
    def test_home_page_returns_200(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_expected_title(self):
        response = self.client.get(reverse('index'))

        self.assertContains(
            response,
            '<title>Holiday Homes</title>',
            html=True
        )
