from django.urls import path

from . import views

app_name = "base_app"

urlpatterns = [
    path("", views.main_route_page, name="main_page"),
    path("about/", views.about, name="about"),
]
