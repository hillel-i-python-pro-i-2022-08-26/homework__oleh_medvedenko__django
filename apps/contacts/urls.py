from django.urls import path

from . import views

app_name = "contacts_app"

urlpatterns = [
    path("", views.get_contacts, name="show_contacts"),
    path("<int:pk>/", views.update_contact, name="contact"),
    path("create/", views.create_contact, name="create"),
    path("update/<int:pk>/", views.update_contact, name="update"),
    path("delete/<int:pk>/", views.delete_contact, name="delete"),
]
