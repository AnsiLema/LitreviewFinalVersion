from django import forms
from django.utils.timezone import deactivate

from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]

class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ["image", "caption"]
