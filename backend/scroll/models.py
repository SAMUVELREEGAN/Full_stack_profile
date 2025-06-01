from django.db import models

class Scroll(models.Model):
    scname = models.CharField(max_length=100)

    def __str__(self):
        return self.scname
    