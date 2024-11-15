from django import forms
from .models import Tweet

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
        