from itertools import chain
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q, CharField, Value
from authentication.models import UserFollows, UserBlocks
from tickets.models import Ticket, Review


@login_required
def home(request):
    """Affiche le fil d'actualité avec abonnements et blocages."""

    # 📌 1. Récupérer les utilisateurs suivis
    followed_users = list(UserFollows.objects.filter(user=request.user)
                          .values_list('followed_user_id', flat=True))

    # 📌 2. Récupérer les utilisateurs bloqués par l'utilisateur connecté
    blocked_users = list(UserBlocks.objects.filter(user=request.user)
                         .values_list('blocked_user_id', flat=True))

    # 📌 3. Récupérer les utilisateurs qui ont bloqué l'utilisateur connecté
    users_who_blocked_me = list(UserBlocks.objects.filter(blocked_user=request.user)
                                .values_list('user_id', flat=True))

    # 🚨 DEBUG : Vérifions ce que l'on récupère
    print(f"✅ Utilisateur : {request.user.username}")
    print(f"📌 Utilisateurs suivis : {followed_users}")
    print(f"❌ Utilisateurs bloqués : {blocked_users}")
    print(f"⛔ Bloqué par : {users_who_blocked_me}")

    # 📌 4. Récupérer les tickets en excluant les utilisateurs bloqués
    tickets = Ticket.objects.filter(
        Q(user=request.user) | Q(user__in=followed_users)  # Inclure les suivis
    ).exclude(
        Q(user__in=blocked_users) | Q(user__in=users_who_blocked_me)  # Exclure les blocages
    ).annotate(post_type=Value("ticket", output_field=CharField()))

    # 📌 5. Récupérer les critiques en excluant les utilisateurs bloqués
    reviews = Review.objects.filter(
        Q(user=request.user) | Q(user__in=followed_users)
    ).exclude(
        Q(user__in=blocked_users) | Q(user__in=users_who_blocked_me)
    ).annotate(post_type=Value("review", output_field=CharField()))

    # 🚨 DEBUG : Vérifions les résultats
    print(f"🎟️ Tickets trouvés : {tickets.count()}")
    print(f"📝 Reviews trouvées : {reviews.count()}")

    # 📌 6. Fusionner et trier les posts par date
    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    # 🚨 DEBUG : Vérifions si des posts sont affichés
    print(f"📌 Nombre total de posts : {len(tickets_and_reviews)}")

    # 📌 7. Ajouter la pagination
    paginator = Paginator(tickets_and_reviews, 5)  # 5 posts par page
    page = request.GET.get("page")
    paged_tickets_and_reviews = paginator.get_page(page)

    # 📌 8. Passer au template
    context = {
        "paged_tickets_and_reviews": paged_tickets_and_reviews,
        "followed_users": followed_users,
        "blocked_users": blocked_users
    }

    return render(request, "reviews/home.html", context=context)
