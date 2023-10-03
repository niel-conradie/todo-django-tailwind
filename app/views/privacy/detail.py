from django.views.generic import DetailView


from app.models import Privacy


class PrivacyDetailView(DetailView):
    model = Privacy
    template_name = "app/privacy/detail.html"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs["slug"])
