from django.shortcuts import redirect, render

from accounts.forms import CustomUserCreationForm


def custom_signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
