<<<<<<< HEAD
from django.urls import path, re_path
=======
from django.urls import path
>>>>>>> acd770417932e8546621d2347c271fd85985426b
from . import views


app_name = "authapp"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
<<<<<<< HEAD
    path("edit/", views.edit, name="edit"),
    re_path(
        r'^verify/(?P<email>.+)/(?P<activation_key>\w+)', 
        views.verify, 
        name='verify'
        ),
=======
     path("edit/", views.edit, name="edit"),
>>>>>>> acd770417932e8546621d2347c271fd85985426b
]
