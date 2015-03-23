from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Category
# Create your tests here.


class CategoryTest(TestCase):
	def create_category(self, category_id = "113", resource_uri = "https://www.eventbriteapi.com/v3/categories",
						name = "Arts", name_localized = "Arts", short_name = "Arts",
						short_name_localized = "Arts"):
		return Category.objects.create(category_id=category_id, resource_uri=resource_uri, name=name, name_localized=name_localized,
									   short_name=short_name, short_name_localized=short_name_localized)

	def test_category_creation(self):
		a = self.create_category()
		self.assertTrue(isinstance(a, Category))

	def test_category_list_view(self):
		a = self.create_category()
		url = reverse('show_cats')
		resp = self.client.get(url)

		self.assertEqual(resp.status_code, 200)
		self.assertIn(a.category_id, resp.content)
		self.assertIn(a.name, resp.content)



