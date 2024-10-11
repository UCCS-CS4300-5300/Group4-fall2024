from django import forms

class QuickTranslateForm(forms.Form):
    q_lang_options = (
        ('', 'Auto-Detect'),
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
