from django.test import TestCase
from mainapp.models import Product, ProductCategory
from django.core.management import call_command




class MainappSmokeTest(TestCase):
    def setUp(self):
        return super().setUp()
   

    def tearDown(self):
        return super().tearDown()

    
    def test_site_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/products/category/0/')
        self.assertEqual(response.status_code, 200)
        for category in ProductCategory.objects.all():
            response = self.client.get(f'/products/category/{category.pk}/')
        self.assertEqual(response.status_code, 200)
        for product in Product.objects.all():
            response = self.client.get(f'/products/product/{product.pk}/')
        self.assertEqual(response.status_code, 200)