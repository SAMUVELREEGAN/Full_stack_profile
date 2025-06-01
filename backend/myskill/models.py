from django.db import models

class Myskill(models.Model):
    pic = models.ImageField(upload_to='myskills/')
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()
    rangecolor = models.CharField(max_length=50)

    def __str__(self):
        return self.name
