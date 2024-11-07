# Generated by Django 4.2.11 on 2024-11-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlm_app', '0010_usersettings_defaultlanguage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlistentry',
            old_name='originalText',
            new_name='sourceText',
        ),
        migrations.RenameField(
            model_name='userlistentry',
            old_name='translatedText',
            new_name='targetText',
        ),
        migrations.RemoveField(
            model_name='userlistentry',
            name='originalLanguage',
        ),
        migrations.RemoveField(
            model_name='userlistentry',
            name='translatedLanguage',
        ),
        migrations.AddField(
            model_name='userlistentry',
            name='sourceLanguage',
            field=models.CharField(choices=[('auto', 'Auto-Detect'), ('en', 'English'), ('fr', 'French'), ('es', 'Spanish'), ('de', 'German'), ('it', 'Italian')], default=('auto', 'Auto-Detect'), max_length=25),
        ),
        migrations.AddField(
            model_name='userlistentry',
            name='targetLanguage',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('es', 'Spanish'), ('de', 'German'), ('it', 'Italian')], default=('en', 'English'), max_length=25),
        ),
    ]
