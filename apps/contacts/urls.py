from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_contacts, name="contacts"),
    path("<int:pk>/", views.edit_contact, name="contacts"),
]
