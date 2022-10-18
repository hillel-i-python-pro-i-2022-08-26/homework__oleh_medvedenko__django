from django.urls import path

from . import views

app_name = "sessions_app"

urlpatterns = [
    path("", views.session_example_view, name="sessions"),
]
