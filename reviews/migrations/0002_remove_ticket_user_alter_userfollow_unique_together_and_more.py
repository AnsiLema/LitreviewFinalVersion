# Generated by Django 5.1.5 on 2025-01-24 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='userfollow',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='userfollow',
            name='followed_user',
        ),
        migrations.RemoveField(
            model_name='userfollow',
            name='user',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
        migrations.DeleteModel(
            name='UserFollow',
        ),
    ]
