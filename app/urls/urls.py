from django.urls import path

from app.views import (
    PrivacyDetailView,
    PrivacyListView,
    TermsDetailView,
    TermsListView,
    HomePageView,
    IndexPageView,
)


app_name = "app"
urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("home/", HomePageView.as_view(), name="home"),
    # Privacy URLs
    path("privacy/", PrivacyListView.as_view(), name="privacy_list"),
    path("privacy/<str:slug>/", PrivacyDetailView.as_view(), name="privacy_detail"),
    # Terms URLs
    path("terms/", TermsListView.as_view(), name="terms_list"),
    path("terms/<str:slug>/", TermsDetailView.as_view(), name="terms_detail"),
]
