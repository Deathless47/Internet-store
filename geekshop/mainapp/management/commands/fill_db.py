from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
<<<<<<< HEAD
=======

# from django.contrib.auth.models import User
>>>>>>> acd770417932e8546621d2347c271fd85985426b
from authapp.models import ShopUser

import json, os

<<<<<<< HEAD
JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')
=======

JSON_PATH = "mainapp/json"


def load_from_json(file_name):
    with open(
        os.path.join(JSON_PATH, file_name + ".json"), "r", encoding="utf-8"
    ) as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json("categories")
>>>>>>> acd770417932e8546621d2347c271fd85985426b

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
<<<<<<< HEAD
            new_category.save()        
        
        products = load_from_json('products')
        
=======
            new_category.save()

        products = load_from_json("products")

>>>>>>> acd770417932e8546621d2347c271fd85985426b
        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
<<<<<<< HEAD
            product['category'] = _category
=======
            product["category"] = _category
>>>>>>> acd770417932e8546621d2347c271fd85985426b
            new_product = Product(**product)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
<<<<<<< HEAD
        ShopUser.objects.create_superuser('admin', 'admin@localhost', 'adminadmin', age=37)

=======
        ShopUser.objects.create_superuser(
            "admin", "admin@localhost", "adminadmin", age=36
        )
>>>>>>> acd770417932e8546621d2347c271fd85985426b
