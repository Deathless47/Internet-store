from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from mainapp import views as mainapp


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path("", include("social_django.urls", namespace="social")),
    path("admin/", include("adminapp.urls", namespace="admin")),
    path("", mainapp.index, name="main"),
    path("contact/", mainapp.contact, name="contact"),
    path("products/", include("mainapp.urls", namespace="products")),
    path("auth/", include("authapp.urls", namespace="auth")),
    path("basket/", include("basketapp.urls", namespace="basket")),
    path("orders/", include("ordersapp.urls", namespace="orders")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)