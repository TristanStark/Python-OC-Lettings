from django.test import TestCase
from django.urls import reverse

from lettings.models import Address
from lettings.models import Letting


class LettingsIndexViewTest(TestCase):
    def test_lettings_index_returns_200(self):
        response = self.client.get(reverse('lettings:index'))

        self.assertEqual(response.status_code, 200)

    def test_lettings_index_contains_expected_title(self):
        response = self.client.get(reverse('lettings:index'))

        self.assertContains(
            response,
            '<title>Lettings</title>',
            html=True
        )


class LettingDetailViewTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street='Main Street',
            city='Irvine',
            state='CA',
            zip_code=92620,
            country_iso_code='USA',
        )
        self.letting = Letting.objects.create(
            title='Test Letting',
            address=self.address,
        )

    def test_letting_detail_returns_200(self):
        response = self.client.get(
            reverse(
                'lettings:letting',
                kwargs={'letting_id': self.letting.id}
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_letting_detail_contains_expected_title(self):
        response = self.client.get(
            reverse(
                'lettings:letting',
                kwargs={'letting_id': self.letting.id}
            )
        )

        self.assertContains(
            response,
            '<title>Test Letting</title>',
            html=True
        )
