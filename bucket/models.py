from django.db import models
from django.utils import timezone
from django.conf import settings

class Item(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=60)
    price = models.FloatField()