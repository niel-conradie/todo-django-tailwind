from django.urls import path

from pages.views import IndexPageView, PrivacyPageView, TermsPageView


app_name = "pages"
urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("privacy/", PrivacyPageView.as_view(), name="privacy"),
    path("terms/", TermsPageView.as_view(), name="terms"),
]
