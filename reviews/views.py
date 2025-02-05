from itertools import chain
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q, CharField, Value
from authentication.models import UserFollows
from tickets.models import Ticket, Review



@login_required
def home(request):
    """View function for feed page of site."""
    followed_users = UserFollows.objects.filter(user=request.user).values_list('followed_user_id', flat=True)
    print(f" suivi par {request.user.username} : {followed_users}")

    # Display tickets (User and followed users)
    tickets = Ticket.objects.filter(
        Q(user=request.user) | Q(user__in=followed_users)
    ).annotate(post_type=Value("ticket", output_field=CharField()))

    # Display reviews (User and followed users)
    reviews = Review.objects.filter(
        Q(user=request.user) | Q(user__in=followed_users)
    ).annotate(post_type=Value("review", output_field=CharField()))


    # Fusion of tickets and reviews, sorted by date of creation (from newest to oldest)
    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    paginator = Paginator(tickets_and_reviews, 5)
    page = request.GET.get("page")
    paged_tickets_and_reviews = paginator.get_page(page)

    context = {
        "paged_tickets_and_reviews": paged_tickets_and_reviews,
        "followed_users": followed_users
    }

    return render(request, "reviews/home.html", context=context)
