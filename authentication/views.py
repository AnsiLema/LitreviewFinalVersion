from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import UserFollows, UserBlocks
from .forms import FollowUserForm

from . import forms

User = get_user_model()


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
    """Allows user to follow a user"""
    form = FollowUserForm(user=request.user)
    message = ""

    if request.method == "POST":
        form = FollowUserForm(request.POST, user=request.user)
        if form.is_valid():
            followed_user = form.cleaned_data["username"]
            UserFollows.objects.get_or_create(user=request.user, followed_user=followed_user)
            message = f"Vous suivez maintenant {followed_user.username}."

    followers = UserFollows.objects.filter(followed_user=request.user)
    followed_users = UserFollows.objects.filter(user=request.user)
    blocked_users = UserBlocks.objects.filter(user=request.user).values_list("blocked_user_id", flat=True)

    return render(
        request,
        "authentication/follow_user_form.html",
        context={
            "form": form,
            "followers": followers,
            "followed_users": followed_users,
            "blocked_users": blocked_users,
            "message": message
        }
    )


@login_required
def unfollow_user(request, user_id):
    """Allows user to unsubscribe from a user"""
    user_to_unfollow = get_object_or_404(User, id=user_id)
    UserFollows.objects.filter(user=request.user, followed_user=user_to_unfollow).delete()
    return redirect("follow_user")


@login_required
def block_user(request, user_id):
    """Allows user to block a user without having to follow them"""
    user_to_block = get_object_or_404(User, id=user_id)

    # Checks if the user is already blocked
    block_relation, created = UserBlocks.objects.get_or_create(
        user=request.user,
        blocked_user=user_to_block
    )

    return redirect("follow_user")


@login_required
def unblock_user(request, user_id):
    user_to_unblock = get_object_or_404(User, id=user_id)
    UserBlocks.objects.filter(user=request.user, blocked_user=user_to_unblock).delete()

    return redirect("follow_user")
