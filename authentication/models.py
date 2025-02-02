from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    follows = models.ManyToManyField("self", symmetrical=False, verbose_name="suit")

class ReviewContributor(models.Model):
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticket = models.ForeignKey("tickets.Ticket", on_delete=models.CASCADE)
    review = models.ForeignKey("tickets.Review", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("contributor", "ticket", "review")


class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following")
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers")
    class Meta:
        unique_together = ("user", "followed_user")
