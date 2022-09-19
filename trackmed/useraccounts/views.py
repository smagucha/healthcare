from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import userupdateform
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm


def signupview(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "useraccounts/signup.html", context)


@login_required(login_url="/accounts/login/")
def useraccount(request):
    if request.method == "POST":
        form = userupdateform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = userupdateform(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "useraccounts/userprofile.html", context)
