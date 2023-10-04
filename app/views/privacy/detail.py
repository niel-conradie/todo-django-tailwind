from django.views.generic import DetailView


from app.models import PrivacyModel


class PrivacyDetailView(DetailView):
    model = PrivacyModel
    template_name = "app/privacy/detail.html"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs["slug"])
