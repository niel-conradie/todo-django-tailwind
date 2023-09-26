from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.forms import CustomLogoutForm


@login_required
def custom_logout_view(request):
    if request.method == "POST":
        form = CustomLogoutForm(data=request.POST)

        if form.is_valid():
            logout(request)
            return redirect(to="pages:index")
    else:
        form = CustomLogoutForm()

    context = {
        "form": form,
    }
    return render(request, template_name="accounts/logout.html", context=context)
