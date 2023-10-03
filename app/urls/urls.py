from django.urls import path

from app.views import (
    PrivacyDetailView,
    PrivacyListView,
    HomePageView,
    IndexPageView,
    TermsPageView,
)


app_name = "app"
urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("home/", HomePageView.as_view(), name="home"),
    path("terms/", TermsPageView.as_view(), name="terms"),
    # Privacy URLs
    path("privacy/", PrivacyListView.as_view(), name="privacy_list"),
    path("privacy/<str:slug>/", PrivacyDetailView.as_view(), name="privacy_detail"),
]
