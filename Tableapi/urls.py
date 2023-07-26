from django.urls import path
from . import views

urlpatterns=[
    path("booktable",views.tableview.as_view()),
    path("canceltable/<int:pk>",views.edittableview.as_view()),
]