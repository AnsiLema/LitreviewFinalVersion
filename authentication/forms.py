from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')

User = get_user_model()


class FollowUserForm(ModelForm):
    class Meta:
        model = User
        fields = ["follows"]




