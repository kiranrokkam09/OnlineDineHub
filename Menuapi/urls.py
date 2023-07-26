from django.urls import path
from . import views

urlpatterns=[
    path('MenuItem',views.MenuItemView.as_view()),
    path('MenuItem/<int:pk>',views.SingleMenuItemView.as_view()),
]