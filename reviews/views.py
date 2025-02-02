from itertools import chain
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q, CharField, Value
from authentication.models import UserFollows
from tickets.models import Ticket, Review

from tickets import models


@login_required
def home(request):
    """View function for feed page of site."""
    followed_users = UserFollows.objects.filter(user=request.user).values_list('followed_user', flat=True)

    # Display tickets (User and followed users)
    tickets = Ticket.objects.filter(
        Q(user=request.user) | Q(contributors__in=followed_users)
    ).annotate(post_type=Value("ticket", output_field=CharField()))

    # Display reviews (User and followed users)
    reviews = Review.objects.filter(
        Q(user=request.user) | Q(ticket__contributors__in=followed_users)
    ).annotate(post_type=Value("review", output_field=CharField()))

    # Fusion of tickets and reviews, sorted by date of creation (from newest to oldest)
    posts = sorted(
        chain(tickets, reviews),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, "reviews/home.html", {"posts": posts})