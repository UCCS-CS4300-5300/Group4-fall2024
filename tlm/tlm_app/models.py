from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Store the translation history of a user
class UserTranslationHistory(models.Model):
    sourceOptions = (
        ('auto', 'Auto-Detect'),
        ('en', 'English'),
        ('fr', 'French'),
        ('es', 'Spanish'),
        ('de', 'German'),
        ('it', 'Italian'),
    )

    targetOptions = (
        ('en', 'English'),
        ('fr', 'French'),
        ('es', 'Spanish'),
        ('de', 'German'),
        ('it', 'Italian'),
    )
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE) # Foriegn key assigned to user for determining unique translation history
    sourceLanguage = models.CharField(max_length=25, default=sourceOptions[0], choices=sourceOptions) # Language of the text that is being translated
    sourceText = models.TextField() # Original text that is being translated
    targetLanguage = models.CharField(max_length=25, default=targetOptions[0], choices=targetOptions) # Language to translate into
    targetText = models.TextField(blank=True) # Text after translation
    dateCreated = models.DateTimeField(auto_now_add=True)
