from django.urls import path

from . import views

app_name = "contacts_app"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="show_contacts"),
    path("create/", views.create_contact, name="create"),
    path("update/<int:pk>/", views.update_contact, name="update"),
    path("delete/<int:pk>/", views.ContactDeleteView.as_view(), name="delete"),
]
