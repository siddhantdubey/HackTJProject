from django.db import models

class Samaritans(models.Model):
    item = models.CharField(max_length=3000000)


class Dogooders(models.Model):
    first_name = models.CharField(max_length=3000000)
    last_name = models.CharField(max_length=3000000)
