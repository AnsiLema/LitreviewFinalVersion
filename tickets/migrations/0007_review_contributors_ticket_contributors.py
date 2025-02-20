# Generated by Django 5.1.5 on 2025-01-31 10:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_reviewcontributor'),
        ('tickets', '0006_delete_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='contributors',
            field=models.ManyToManyField(related_name='review_contributions', through='authentication.ReviewContributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='contributors',
            field=models.ManyToManyField(related_name='ticket_contributions', through='authentication.ReviewContributor', to=settings.AUTH_USER_MODEL),
        ),
    ]
