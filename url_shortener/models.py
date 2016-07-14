import random, string
from django.db import models


class Link(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    clicks_count = models.PositiveIntegerField(default=0)

    def create_short_url(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.create_short_url()
        super(Link, self).save(*args, **kwargs)