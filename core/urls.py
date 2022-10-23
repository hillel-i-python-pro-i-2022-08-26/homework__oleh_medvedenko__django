from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.base.urls")),
    path("users/", include("apps.users.urls")),
    path("contacts/", include("apps.contacts.urls")),
    path("sessions/", include("apps.sessions_app.urls")),
]
