from django.db import models


class Link(models.Model):
    long_url = models.URLField()
    short = models.CharField(max_length=20)
    created = models.DateTimeField()
    clicks_count = models.PositiveIntegerField()
