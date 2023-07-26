from django.urls import path
from . import views
from rest_framework.authtoken import views as tokenviews
urlpatterns=[
    path("register",views.registerview.as_view()),
    path("login",tokenviews.obtain_auth_token),
    path("logout",views.logoutview.as_view()),
]