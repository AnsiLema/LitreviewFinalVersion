from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from PIL import Image as ResizeImage

IMAGE_MAX_SIZE = (250, 250)


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def resize_image(self):
        if not self.image or not self.image.path:
            return
        image = ResizeImage.open(self.image)
        image.thumbnail(IMAGE_MAX_SIZE)
        image.save(self.image.path)


class Review(models.Model):
    ticket = models.ForeignKey(to="Ticket", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def resize_image(self):
        if not self.image or not self.image.path:
            return

        image = ResizeImage.open(self.image)
        image.thumbnail(IMAGE_MAX_SIZE)
        image.save(self.image.path)
