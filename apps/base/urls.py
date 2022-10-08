from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_route_page, name="index"),
    path("generate-users/", views.users_info, name="index"),
    path("generate-users/<int:number>/", views.users_info, name="index"),
]
