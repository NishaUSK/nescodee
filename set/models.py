from django.conf import settings
from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class Company(models.Model):
#     ceo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     status = models.CharField(max_length=200)
#     launched_date = models.DateTimeField(blank=True, null=True)
#
#     def launch(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.status
