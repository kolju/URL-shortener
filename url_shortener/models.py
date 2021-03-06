import random, string
from django.db import models
from django.db import IntegrityError


class Link(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    clicks_count = models.PositiveIntegerField(default=0)


    class Meta:
        index_together = [
            ["clicks_count", "created"],
        ]

    @staticmethod
    def create_short_url():
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

    def save(self, *args, **kwargs):
        while True:
            if not self.short_url:
                self.short_url = self.create_short_url()

            try:
                super(Link, self).save(*args, **kwargs)
            except IntegrityError:
                pass
            else:
                break

    def __str__(self):
        return self.short_url

