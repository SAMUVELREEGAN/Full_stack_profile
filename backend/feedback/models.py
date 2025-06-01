# models.py
from django.db import models

class SocialLink(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name
