<<<<<<< HEAD
import random


from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage



# MENU_LINKS = [
#     {"url": "main", "active": ["main"], "name": "домой"},
#     {"url": "products:all", "active": ["products:all", "products.category"], "name": "продукты"},
#     {"url": "contact", "active": ["contact"], "name": "контакты"},
# ]
=======
from django.shortcuts import render
import json

from .models import Product, ProductCategory


MENU_LINKS = [
    {"url": "main", "name": "домой"},
    {"url": "products:products", "name": "продукты"},
    {"url": "contact", "name": "контакты"},
]
>>>>>>> acd770417932e8546621d2347c271fd85985426b


def index(request):
    products = Product.objects.all()[:4]
    return render(
        request,
        "mainapp/index.html",
<<<<<<< HEAD
        context={"title": "Главная", "products": products},
    )


def get_hot_product(queryset):
    return random.choice(queryset)
=======
        context={"title": "Главная", "menu_links": MENU_LINKS, "products": products},
    )
>>>>>>> acd770417932e8546621d2347c271fd85985426b


def products(request):
    categories = ProductCategory.objects.all()
<<<<<<< HEAD
    products = Product.objects.all()
    hot_product = get_hot_product(products)
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты", 
            "hot_product": hot_product,
            "products": products.exclude(pk=hot_product.pk)[:4],
            "categories": categories,
        },
    )

def category(request, category_id, page=1):
    categories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, id=category_id)
    products = Product.objects.filter(category=category)
    hot_product = get_hot_product(products)
    paginator = Paginator(products.exclude(pk=hot_product.pk), 3)
    try:
        products_page = paginator.page(page)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)   

    
=======
    with open("./products.json", "r") as file:
        products = json.load(file)

>>>>>>> acd770417932e8546621d2347c271fd85985426b
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты",
<<<<<<< HEAD
            "hot_product": get_hot_product(products),
            "paginator": paginator,
            "page": products_page,
            "products": products_page,
            "category": category,
=======
            "products": products,
            "menu_links": MENU_LINKS,
>>>>>>> acd770417932e8546621d2347c271fd85985426b
            "categories": categories,
        },
    )

<<<<<<< HEAD
def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = ProductCategory.objects.all()
    
    return render(
        request,
        "mainapp/product.html",
        context={
            "title": "Продукты",
            "product": product,
            "categories": categories,
        },
    )
=======

def category(request, pk):
    return products(request)
>>>>>>> acd770417932e8546621d2347c271fd85985426b


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
<<<<<<< HEAD
=======
            "menu_links": MENU_LINKS,
>>>>>>> acd770417932e8546621d2347c271fd85985426b
        },
    )
