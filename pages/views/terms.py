from django.views.generic import TemplateView


class TermsPageView(TemplateView):
    template_name = "pages/terms.html"
