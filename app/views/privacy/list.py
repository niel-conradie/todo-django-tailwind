from django.views.generic import ListView


from app.models import Privacy


class PrivacyListView(ListView):
    model = Privacy
    template_name = "app/privacy/list.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")
