from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="index"),
    path("<int:id>", views.index, name="index"),
    path("Django/", views.django, name="django"),
    path("Flask/", views.flask, name="flask"),
    path("Pygame/", views.pygame, name="pygame"),
    path("Linux_Git/", views.git_Linux, name="git_Linux"),
    path("PyQt5/", views.pyQt5, name="pyQt5"),
    path("Something_new/", views.something_new, name="something_new"),
]