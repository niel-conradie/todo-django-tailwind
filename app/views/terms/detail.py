from django.views.generic import DetailView


from app.models import TermsModel


class TermsDetailView(DetailView):
    model = TermsModel
    template_name = "app/terms/detail.html"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs["slug"])
