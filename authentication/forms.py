from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import UserFollows


User = get_user_model()


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "email",
        )


class FollowUserForm(forms.ModelForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': "Rechercher un utilisateur..."}
        )
    )

    class Meta:
        model = UserFollows
        fields = ["username"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(FollowUserForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user_to_follow = User.objects.get(username=username)
            if user_to_follow == self.user:
                raise forms.ValidationError("Vous ne pouvez pas vous suivre vous-même !")

            return user_to_follow

        except User.DoesNotExist:
            raise forms.ValidationError("Cet utilisateur n'existe pas.")
