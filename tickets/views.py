from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm
from .models import Ticket, Review
from django.contrib.auth.decorators import login_required

from . import forms

@login_required
def ticket_list(request):
    tickets = Ticket.objects.all().order_by('-time_created')
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})

@login_required
def ticket_create(request):
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("ticket_list")
    return render(request, "tickets/ticket_create.html", {"form": forms.TicketForm()})


@login_required
def ticket_update(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    form = forms.TicketForm(instance=ticket)
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.save()
            return redirect("ticket_list")
        else:
            form = forms.TicketForm(instance=ticket)

    return render(request, "tickets/ticket_update.html", {"form": form, "ticket": ticket})


def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        ticket.delete()
        return redirect("ticket_list")

    return render(request, "tickets/ticket_confirm_delete.html", {"ticket": ticket})



@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    reviews = Review.objects.filter(ticket=ticket)
    return render(request, "tickets/ticket_detail.html", {"ticket": ticket, "reviews": reviews})


def image_upload(request):
    form = forms.ImageForm()
    if request.method == "POST":
        form = forms.ImageForm(request.POST, request.FILES)
        image = form.save(commit=False)
        image.uploader = request.user
        image.save()
        return redirect("ticket_list")

    return render(request, "tickets/image_upload.html", {"form": form})


@login_required
def ticket_and_review_upload(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST, request.FILES)
        if any([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("home")
    context = {
        "ticket_form": ticket_form,
        "review_form": review_form,
    }
    return render(request, "tickets/ticket_and_review_upload.html", context=context)

@login_required
def review_create(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if Review.objects.filter(ticket=ticket, user=request.user).exists():
        return redirect("ticket_detail", ticket_id)

    form = forms.ReviewForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("ticket_detail", ticket_id)

    return render(request, "tickets/review_create.html", {"form": form, "ticket": ticket})

@login_required
def review_update(request, ticket_id, review_id):
    review = get_object_or_404(Review, ticket_id=ticket_id, id=review_id)
    if review.user != request.user:
        return HttpResponseForbidden("Vous ne pouyez modifier que vos propres critiques.")
    form = forms.ReviewForm(instance=review)
    if request.method == "POST":
        form = forms.ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect("ticket_detail", review.ticket.id)
        else:
            form = forms.ReviewForm(instance=review)

    return render(request, "tickets/review_update.html", {"form": form, "review": review})

@login_required
def review_delete(request, ticket_id, review_id):
    review = get_object_or_404(Review, ticket_id=ticket_id, id=review_id)
    if review.user != request.user:
        HttpResponseForbidden("Vous ne pouyez supprimer que vos propres critiques.")
    if request.method == "POST":
        review.delete()
        return redirect("ticket_detail", ticket_id= review.ticket.id)

    return render(request, "tickets/review_confirm_delete.html", {"review": review,
                                                                  "ticket": review.ticket})