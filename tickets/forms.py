from django import forms

from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]
"""
class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ["image", "caption"]
"""
class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ["headline", "body", "rating", "image", ]
        widgets = {
            "headline": forms.TextInput(attrs={"class": "form-control"}),
            "rating": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 5}),
        }