from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class QuickTranslateForm(forms.Form):
    q_lang_options = (
        ('auto', 'Auto-Detect'),
        ('en', 'English'),
        ('fr', 'French'),
        ('es', 'Spanish'),
        ('de', 'German'),
        ('it', 'Italian'),
    )

    t_lang_options = (
        ('en', 'English'),
        ('fr', 'French'),
        ('es', 'Spanish'),
        ('de', 'German'),
        ('it', 'Italian'),
    )

    q_lang = forms.ChoiceField(label='Source Language', required=False, choices=q_lang_options)
    q_text = forms.CharField()
    t_lang = forms.ChoiceField(choices=t_lang_options)
    t_text = forms.CharField(required=False)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']