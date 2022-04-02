import random
from django.core.cache import cache
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.cache import cache_page



# MENU_LINKS = [
#     {"url": "main", "active": ["main"], "name": "домой"},
#     {"url": "products:all", "active": ["products:all", "products.category"], "name": "продукты"},
#     {"url": "contact", "active": ["contact"], "name": "контакты"},
# ]


def index(request):
    products = Product.objects.all()[:4]
    return render(
        request,
        "mainapp/index.html",
        context={"title": "Главная", "products": products},
    )


def get_hot_product(queryset):
    return random.choice(queryset)


def get_categories():
    if settings.LOW_CACHE:
        KEY = 'all_categories'
        categories = cache.get(KEY)
        if not categories:
            categories = ProductCategory.objects.all()
            cache.set(KEY, categories)
        return categories
    else:
        return ProductCategory.objects.all()
 

def products(request):
    categories = get_categories()
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
    categories = get_categories()
    category = get_object_or_404(ProductCategory, id=category_id)
    products = Product.objects.filter(category=category, is_active=True)
    hot_product = get_hot_product(products)
    paginator = Paginator(products.exclude(pk=hot_product.pk), 3)
    try:
        products_page = paginator.page(page)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)   

    
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "hot_product": get_hot_product(products),
            "paginator": paginator,
            "page": products_page,
            "products": products_page,
            "category": category,
            "categories": categories,
        },
    )

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = get_categories()
    
    return render(
        request,
        "mainapp/product.html",
        context={
            "title": "Продукты",
            "product": product,
            "categories": categories,
        },
    )

# @cache_page(3600)
def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
        },
    )
