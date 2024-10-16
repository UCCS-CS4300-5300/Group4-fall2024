# Generated by Django 4.2.11 on 2024-10-17 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlm_app', '0005_alter_usertranslationhistory_sourcelanguage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertranslationhistory',
            name='sourceLanguage',
            field=models.CharField(choices=[('auto', 'Auto-Detect'), ('en', 'English'), ('fr', 'French'), ('es', 'Spanish'), ('de', 'German'), ('it', 'Italian')], default=('auto', 'Auto-Detect'), max_length=25),
        ),
        migrations.AlterField(
            model_name='usertranslationhistory',
            name='targetLanguage',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('es', 'Spanish'), ('de', 'German'), ('it', 'Italian')], default=('en', 'English'), max_length=25),
        ),
    ]
