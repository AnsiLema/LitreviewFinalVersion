from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from . import forms

def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "authentication/signup.html", context={'form': form})

@login_required
def follow_user(request):
    form = forms.FollowUserForm(instance=request.user)
    if request.method == "POST":
        form = forms.FollowUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "authentication/follow_user_form.html", context={'form': form})
