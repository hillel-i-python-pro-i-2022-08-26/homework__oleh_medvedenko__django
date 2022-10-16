from django.urls import path

from . import views

urlpatterns = [
    path("", views.users_info, name="users"),
    path("<int:number>/", views.users_info, name="users"),
]
