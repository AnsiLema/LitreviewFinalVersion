from itertools import chain
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q, CharField, Value
from authentication.models import UserFollows, UserBlocks
from tickets.models import Ticket, Review


@login_required
def home(request):
    """Shows the news feed with subscriptions and blocks."""

    followed_users = list(UserFollows.objects.filter(user=request.user)
                          .values_list('followed_user_id', flat=True))

    blocked_users = list(UserBlocks.objects.filter(user=request.user)
                         .values_list('blocked_user_id', flat=True))

    users_who_blocked_me = list(UserBlocks.objects.filter(blocked_user=request.user)
                                .values_list('user_id', flat=True))

    tickets = Ticket.objects.filter(
        Q(user=request.user) | Q(user__in=followed_users)  # Inclure les suivis
    ).exclude(
        Q(user__in=blocked_users) | Q(user__in=users_who_blocked_me)  # Exclure les blocages
    ).annotate(post_type=Value("ticket", output_field=CharField()))

    reviews = Review.objects.filter(
        Q(user=request.user) |
        Q(user__in=followed_users) |
        Q(ticket__user=request.user)
    ).exclude(
        Q(user__in=blocked_users) | Q(user__in=users_who_blocked_me)
    ).annotate(post_type=Value("review", output_field=CharField()))


    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    paginator = Paginator(tickets_and_reviews, 5)  # 5 posts par page
    page = request.GET.get("page")
    paged_tickets_and_reviews = paginator.get_page(page)

    context = {
        "paged_tickets_and_reviews": paged_tickets_and_reviews,
        "followed_users": followed_users,
        "blocked_users": blocked_users
    }

    return render(request, "reviews/home.html", context=context)
