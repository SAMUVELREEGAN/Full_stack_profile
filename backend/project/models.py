from django.db import models

class Project(models.Model):
    pic = models.ImageField(upload_to='projects/')
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    description = models.TextField()
    link_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

