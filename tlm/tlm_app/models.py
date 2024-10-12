from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Store the translation history of a user
class UserTranslationHistory(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE) # Foriegn key assigned to user for determining unique translation history
    originalLanguage = models.CharField(max_length=255) # Language of the text that is being translated
    translatedIntoLanguage = models.CharField(max_length=255) # Language to translate into
    originalText = models.TextField() # Original text that is being translated
    translatedText = models.TextField() # Text after translation 