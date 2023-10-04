from django.views.generic import ListView


from app.models import TermsModel


class TermsListView(ListView):
    model = TermsModel
    template_name = "app/terms/list.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")
