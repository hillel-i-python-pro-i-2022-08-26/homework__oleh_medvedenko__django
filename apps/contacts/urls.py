from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "contacts_app"

router = routers.DefaultRouter()
router.register(r"hyper", views.ContactsViewSet)

urlpatterns = [
    path("", views.ContactList.as_view(), name="show_contacts"),
    path("create/", views.ContactCreate.as_view(), name="create_contact"),
    path("update/<int:pk>/", views.ContactUpdate.as_view(), name="update_contact"),
    path("delete/<int:pk>/", views.ContactDelete.as_view(), name="delete_contact"),
    # Model Serializers
    path("api/v1/list/", views.ContactAPIList.as_view(), name="show_API_contacts"),
    path("api/v1/edit/<int:pk>/", views.ContactAPIEdit.as_view(), name="update_API_contact"),
    # Hyperlinked Model Serializer
    path("api/v1/", include(router.urls)),
]
