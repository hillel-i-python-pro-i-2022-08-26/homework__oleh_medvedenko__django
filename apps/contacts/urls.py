from django.urls import path

from . import views

app_name = "contacts_app"

urlpatterns = [
    path("", views.ContactList.as_view(), name="show_contacts"),
    path("create/", views.ContactCreate.as_view(), name="create_contact"),
    path("update/<int:pk>/", views.ContactUpdate.as_view(), name="update_contact"),
    path("delete/<int:pk>/", views.ContactDelete.as_view(), name="delete_contact"),
]
