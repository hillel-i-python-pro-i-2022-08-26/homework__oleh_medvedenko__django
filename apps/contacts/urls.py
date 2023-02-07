from django.urls import path

from . import views

app_name = "contacts_app"

urlpatterns = [
    path("", views.ContactList.as_view(), name="show_contacts"),
    path("create/", views.ContactCreate.as_view(), name="create_contact"),
    path("update/<int:pk>/", views.ContactUpdate.as_view(), name="update_contact"),
    path("delete/<int:pk>/", views.ContactDelete.as_view(), name="delete_contact"),
    path("api/v1/list/", views.ContactAPIList.as_view(), name="show_API_contacts"),
    path("api/v1/list/<int:pk>/", views.ContactAPIList.as_view(), name="show_API_contacts"),
    path("api/v1/edit/<int:pk>/", views.ContactAPIEdit.as_view(), name="update_API_contact"),
]
