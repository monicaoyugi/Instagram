from django.test import TestCase, Client
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='monica', email = 'monica@gmail.com', password = 'Password123')
        self.user.save()

        self.profile_test = Profile(id=1, name='image', profile_picture='default.jpg', bio='this is a test profile',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_secure_page(self):
        trial = User.objects.all()
        c = Client()
        print(c.login(username='monica', password='Password123'))
        print("*************************")
        response = c.get('/', follow=True)
        print(response)
        print("*******************************")
        user = User.objects.get(username='charles')
        self.assertEqual(response.status_code, 200)