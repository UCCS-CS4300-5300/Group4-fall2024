from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserTranslationHistory

class QuickTranslateForm(forms.ModelForm):
    class Meta:
        model = UserTranslationHistory
        fields = ['sourceLanguage', 'sourceText', 'targetLanguage', 'targetText']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']
