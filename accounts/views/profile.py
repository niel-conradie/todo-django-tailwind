from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


CustomUser = get_user_model()


@login_required
def custom_profile_view(request, pk):
    user = CustomUser.objects.get(id=pk)

    context = {
        "user": user,
    }
    return render(request, "accounts/profile.html", context)
