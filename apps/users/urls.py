from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path("", views.users_info, name="users"),
    path("<int:number>/", views.users_info, name="users_amount"),
]
