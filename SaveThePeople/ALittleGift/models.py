from django.db import models
from django.conf import settings
from django.urls import reverse
from django_google_maps import fields as map_fields
from geoposition.fields import GeopositionField

class Samaritans(models.Model):
    item = models.CharField(max_length=3000000)


class Dogooders(models.Model):
    first_name = models.CharField(max_length=3000000)
    last_name = models.CharField(max_length=3000000)

class Request(models.Model):
    message = models.CharField(max_length=30000)
    date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=300)
    location = GeopositionField(blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse('request_detail', args=[str(self.id)])

    def __str__(self):
        return self.message
