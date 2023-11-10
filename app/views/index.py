from django.shortcuts import render


def index_page_view(request):
    context = {}
    return render(request, "app/index.html", context)
