from django.db import models


class Moof(models.Model):

    title = models.CharField(
        unique=True,
        max_length=50,
    )

    published = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title