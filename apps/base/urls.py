from django.urls import path

from . import views

urlpatterns = [path("", views.main_route_page, name="main_route_page"), path("about/", views.about, name="about")]
