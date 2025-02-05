from django import forms

from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]
        labels = {
            "title": "Titre du Livre",
            "description": "Description",
            "image": "Ajouter une Image (optionnel)"
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "image": forms.FileInput(attrs={"class": "form-control"})
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ["headline", "body", "rating", "image", ]
        widgets = {
            "headline": forms.TextInput(attrs={"class": "form-control"}),
            "rating": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 5}),
            "body": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }
        labels = {
            "headline": "Titre de la Critique",
            "body": "Contenu de la Critique",
            "rating": "Note",
            "image": "Ajouter une Image (optionnel)"
        }
