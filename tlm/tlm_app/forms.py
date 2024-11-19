from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserTranslationHistory


class QuickTranslateForm(forms.ModelForm):
    class Meta:
        model = UserTranslationHistory
        fields = [
            'sourceLanguage', 'sourceText', 'targetLanguage', 'targetText'
            ]
        widgets = {
            'sourceLanguage':
                forms.Select(attrs={'class': 'form-control'}),
            'sourceText':
                forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'targetLanguage':
                forms.Select(attrs={'class': 'form-control'}),
            'targetText':
                forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
