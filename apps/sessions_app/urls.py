from django.urls import path

from . import views

app_name = "sessions_app"

urlpatterns = [
    path("", views.AllInfoViews.as_view(), name="all_info"),
    path("session/<slug:session_key>/", views.SessionInfoViews.as_view(), name="session_info"),
    path("user/<int:pk>/", views.UserInfoViews.as_view(), name="user_info"),
]
