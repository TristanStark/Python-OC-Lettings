from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from profiles.models import Profile


class ProfilesIndexViewTest(TestCase):
    def test_profiles_index_returns_200(self):
        response = self.client.get(reverse('profiles:index'))

        self.assertEqual(response.status_code, 200)

    def test_profiles_index_contains_expected_title(self):
        response = self.client.get(reverse('profiles:index'))

        self.assertContains(
            response,
            '<title>Profiles</title>',
            html=True
        )


class ProfileDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='test-password',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Irvine',
        )

    def test_profile_detail_returns_200(self):
        response = self.client.get(
            reverse(
                'profiles:profile',
                kwargs={'username': self.user.username}
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_profile_detail_contains_expected_title(self):
        response = self.client.get(
            reverse(
                'profiles:profile',
                kwargs={'username': self.user.username}
            )
        )

        self.assertContains(
            response,
            '<title>testuser</title>',
            html=True
        )
