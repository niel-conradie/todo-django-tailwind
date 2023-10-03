from django.views.generic import TemplateView


class TermsPageView(TemplateView):
    template_name = "app/terms.html"
