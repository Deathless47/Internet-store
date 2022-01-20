
from itertools import product
import json
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta


MENU_LINKS = [
    {'url': 'main', 'name': 'домой'},
    {'url': 'products', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'}
]


def index(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'menu_links': MENU_LINKS,
        'now_time': timezone.now()
    })


def products(request):
    with open('./products.json', 'r') as file:
        products = json.load(file)

    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'products': products,
        'menu_links': MENU_LINKS,
        'now_time': timezone.now()
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,
        'now_time': timezone.now()
    })
