from django.urls import reverse

from rest_framework.test import APIClient, APITestCase


class HeroViewsetsTest(APITestCase):

    fixtures = ('heroes',)

    def test_heroes_list_correct(self):
        response = self.client.get(reverse('heroes-list'))

        data = response.json()
        # print(data)
        # [{'id': 1, 'name': 'Bruce Wayne', 'alias': 'Batman'}, {'id': 2, 'name': 'Clark Kent', 'alias': 'Superman'}]
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(data), 2)

    def test_heroes_detail_correct(self):
        response = self.client.get(reverse('heroes-detail', kwargs={"pk":1}))

        data = response.json()

        # print(data)
        # {'id': 1, 'name': 'Bruce Wayne', 'alias': 'Batman'}

        self.assertEqual(response.status_code, 200)

        self.assertEqual(data["name"], "Bruce Wayne")

