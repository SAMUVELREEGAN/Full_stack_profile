from django.db import models

class Service(models.Model):
    pic = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=255)
    contant = models.TextField()

    def __str__(self):
        return self.title
