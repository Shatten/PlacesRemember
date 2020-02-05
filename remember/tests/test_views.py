from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from remember.models import Remember


class RememberViewTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(username='test_user', password='123', email='test@test.ru')
        test_user2 = User.objects.create_user(username='test_user2', password='321', email='test@test.ru')
        test_remember1 = Remember.objects.create(title='test1', description='test_desc1', map_coordinates='0.0;0.1',
                                                 id_user=test_user)
        test_remember2 = Remember.objects.create(title='test2', description='test_desc2', map_coordinates='0.0;0.2')
        test_remember1.save()
        test_remember2.save()

    def test_get_remembers_for_login_user(self):
        is_login = self.client.login(username='test_user', password='123')
        response = self.client.get(reverse('remembers'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context_data['object_list']), 1)

    def test_links_for_not_login_user(self):
        response = self.client.get(reverse('remembers'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('add_remember'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)

    def test_create_remember(self):
        is_login = self.client.login(username='test_user2', password='321')
        response = self.client.post(reverse('add_remember'),
                                    {'title': 'test_title', 'description': 'test_desc', 'map_coordinates': '0.0;0.1'})
        response = self.client.get(reverse('remembers'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context_data['object_list']), 1)
        self.assertEqual('test_title', response.context_data.get('object_list')[0].title)

