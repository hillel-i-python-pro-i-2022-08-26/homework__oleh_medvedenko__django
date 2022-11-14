from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.base.urls")),
    path("users/", include("apps.users.urls")),
    path("contacts/", include("apps.contacts.urls")),
    path("sessions/", include("apps.sessions_app.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
