from django.contrib import admin
from .models import UserTranslationHistory, UserListObject, UserListEntry

# Register your models here.
admin.site.register(UserTranslationHistory)
admin.site.register(UserListObject)
admin.site.register(UserListEntry)
