from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from tickets import models

@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'reviews/home.html', {'tickets': tickets})
