from django.test import TestCase
from django.test.client import Client
from django.template import Context
from django.core.urlresolvers import reverse
from django_any import any_model
from datetime import date

from testapp.models import PersonalInfo


class MainPageTest(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.my_personal_info = PersonalInfo.objects.get(pk=1)
        self.client = Client()

    def test_obj_as_string(self):
        self.assertEqual(str(self.my_personal_info), 'Andrew Gordiychuk')

    def test_models_fields(self):
        self.assertEqual(self.my_personal_info.name, 'Andrew')
        self.assertEqual(self.my_personal_info.last_name, 'Gordiychuk')
        self.assertEqual(self.my_personal_info.bio, 'Nothing interesting is here')
        self.assertEqual(self.my_personal_info.email, 'annima.sola@gmail.com')
        self.assertEqual(self.my_personal_info.jabber, 'annima@khavr.com')
        self.assertEqual(self.my_personal_info.skype, 'gorazio1986')
        self.assertEqual(self.my_personal_info.other_contacts,
                    'gorazio@ukr.net')
        self.assertEqual(self.my_personal_info.birth_date,
                    date(1986, 12, 20))

    def test_object_delete(self):
        self.my_personal_info.delete()
        self.assertTrue(PersonalInfo.objects.filter(name='Andrew').count() \
                    == 0)

    def test_template_context(self):
        response = self.client.get(reverse('mainpage_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainpage.html')

    def test_template(self):
        response = self.client.get(reverse('mainpage_url'))
        self.assertContains(response, 'Assignment', status_code=200)
        self.assertContains(response, self.my_personal_info.name,
                    status_code=200)
        self.assertContains(response, self.my_personal_info.last_name,
                    status_code=200)
        self.assertContains(response, self.my_personal_info.bio,
                    status_code=200)
        self.assertContains(response, self.my_personal_info.email,
                    status_code=200)
        self.assertContains(response, self.my_personal_info.jabber,
                    status_code=200)
        self.assertContains(response, self.my_personal_info.skype,
                    status_code=200)
        self.assertContains(response, self.my_personal_info.other_contacts,
                    status_code=200)

    def test_context(self):
        response = self.client.get(reverse('mainpage_url'))
        self.assertTrue('my_data' in response.context)
        self.assertTrue(self.my_personal_info.name in
                    str(response.context['my_data']))
