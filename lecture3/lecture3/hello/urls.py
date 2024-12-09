from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("rohit", views.rohit, name="rohit"),
    path("estaa", views.estaa, name="estaa")
]