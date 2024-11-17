from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control rounded border border-secondary shadow-sm p-3',
                'rows': 5,
                'placeholder': "What's on your mind?",
                'style': 'resize: none;',
            }),
        }
        
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control rounded border border-secondary shadow-sm p-3',
                'placeholder': 'Username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control rounded border border-secondary shadow-sm p-3',
                'placeholder': 'Email',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control rounded border border-secondary shadow-sm p-3',
                'placeholder': 'Password',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control rounded border border-secondary shadow-sm p-3',
                'placeholder': 'Confirm Password',
            }),
        }
        
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control rounded border border-secondary shadow-sm p-3',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control rounded border border-secondary shadow-sm p-3',
        'placeholder': 'Password',
    }))