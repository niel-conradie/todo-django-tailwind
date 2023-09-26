from django.shortcuts import redirect, render

from accounts.forms import CustomUserCreationForm


def custom_signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(to="accounts:login")
    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
    }
    return render(request, template_name="accounts/signup.html", context=context)
