from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=63)
    password = forms.CharField(label="Mot de Passe", widget=forms.PasswordInput, max_length=63)