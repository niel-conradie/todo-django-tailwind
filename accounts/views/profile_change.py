from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render

from accounts.forms import CustomUserChangeForm


CustomUser = get_user_model()


def custom_profile_change_view(request, pk):
    user = CustomUser.objects.get(id=pk)

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect("accounts:profile", pk=user.id)
    else:
        form = CustomUserChangeForm(instance=user)

    context = {
        "form": form,
    }
    return render(request, "accounts/profile_change.html", context)
