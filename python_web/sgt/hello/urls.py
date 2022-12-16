from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jayan", views.jayan,name ="jayan"),
    path("gus",views.gus, name="gus"),
    path("<str:name>", views.greet, name ="greet"),
]
