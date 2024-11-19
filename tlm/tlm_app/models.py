from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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


# Store the translation history of a user
class UserTranslationHistory(models.Model):
    # Foriegn key assigned to user for determining unique translation history
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    # Language of the text that is being translated
    sourceLanguage = models.CharField(
        max_length=25, default=sourceOptions[0], choices=sourceOptions
    )

    # Original text that is being translated
    sourceText = models.TextField()
    # Language to translate into
    targetLanguage = models.CharField(
        max_length=25, default=targetOptions[0], choices=targetOptions
    )

    # Text after translation
    targetText = models.TextField(blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.dateCreated}"

    def save(self, *args, **kwargs):
        history = UserTranslationHistory.objects.filter(user=self.user)
        if (num := history.count() - 10) >= 0:
            for i in range(num + 1):
                history[i].delete()
        super().save(*args, **kwargs)


# Store a user's created lists
class UserListObject(models.Model):
    # User that created list
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    listTitle = models.CharField(max_length=255)  # Title of list

    # Returns User List for use in foreign keys
    def __str__(self):
        return f"{self.listTitle} {self.user}"


# Entries in a user created list
class UserListEntry(models.Model):
    # Assigns list entry to a list
    userList = models.ForeignKey(UserListObject, on_delete=models.CASCADE)
    # Language of the text that is being translated
    sourceLanguage = models.CharField(
        max_length=25, default=sourceOptions[0], choices=sourceOptions
    )
    sourceText = models.TextField()  # Original text that is being translated
    # Language to translate into
    targetLanguage = models.CharField(
        max_length=25, default=targetOptions[0], choices=targetOptions
    )
    targetText = models.TextField(blank=True)  # Text after translation

    def __str__(self):
        return f"{self.userList}"


# Store the user's prefered settings
class UserSettings(models.Model):
    # Enforces a one-to-one relationship
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )  # Foreign key pointing to user to assign settings profile
    # User preference for dark mode on or off
    darkModeToggle = models.BooleanField(default=False)
    # User preference for default language to translate into
    defaultLanguage = models.CharField(max_length=25, default="English")

    def __str__(self):
        return f"{self.user}"
