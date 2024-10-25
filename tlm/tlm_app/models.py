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

    def save(self, *args, **kwargs):
        history = UserTranslationHistory.objects.filter(user=self.user)
        if (num := history.count() - 10) >= 0:
            for i in range(num + 1):
                history[i].delete()
        super().save(*args, **kwargs)

# Store a user's created lists
class UserListObject(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE) # User that created list
    listTitle = models.CharField(max_length=255) # Title of list 

    # Returns User List for use in foreign keys
    def __str__(self):
        return f"{self.listTitle} {self.user}"

# Entries in a user created list 
class UserListEntry(models.Model):
    userList = models.ForeignKey(UserListObject, on_delete=models.CASCADE) # Assigns list entry to a list
    originalLanguage = models.CharField(max_length=25) # Language of the text that is being translated
    originalText = models.TextField() # Original text that is being translated
    translatedLanguage = models.CharField(max_length=25) # Language to translate into
    translatedText = models.TextField(blank=True) # Text after translation

# Store the user's prefered settings
class UserSettings(models.Model):
    # Enforces a one-to-one relationship
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True, 
    ) # Foreign key pointing to user to assign settings profile
    darkModeToggle = models.BooleanField(default=False) # User preference for dark mode on or off