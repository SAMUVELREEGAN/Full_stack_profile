# models.py
from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=255)
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
