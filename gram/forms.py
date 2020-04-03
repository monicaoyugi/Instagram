from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from gram.models import Profile, Comment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','profile_caption']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author','post','body']