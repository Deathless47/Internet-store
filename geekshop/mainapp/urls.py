from django.urls import path
from . import views

<<<<<<< HEAD


app_name = 'mainapp'

urlpatterns = [
    path("", views.products, name="all"),
    path("<int:category_id>", views.category, name="category"),
    path("<int:category_id>/<int:page>", views.category, name="paged_category"),
    path("product/<int:product_id>", views.product, name="product"),
]
=======
app_name = "mainapp"

urlpatterns = [
    path("", views.products, name="products"),
    path("<int:pk>", views.category, name="category"),
]
>>>>>>> acd770417932e8546621d2347c271fd85985426b
