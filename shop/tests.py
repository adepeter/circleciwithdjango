import pytest
from django.test import TestCase

# Create your tests here.
from shop.models import Shop


class ShopTestCase(TestCase):

    def test_shop_creation(self):
        first_shop = Shop.objects.create(name='Ice cream')
        second_shop = Shop.objects.create(name='Second Shop')
        self.assertEqual(Shop.objects.count(), 2)
        self.assertQuerysetEqual(Shop.objects.all().order_by('id'), [first_shop, second_shop])
