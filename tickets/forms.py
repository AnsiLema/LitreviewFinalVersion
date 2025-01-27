from django import forms

from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]

class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ["image", "caption"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ["headline", "body", "rating", "image", ]