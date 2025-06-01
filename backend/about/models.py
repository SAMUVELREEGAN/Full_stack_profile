from django.db import models

class About(models.Model):
    question = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    pic = models.ImageField(upload_to='about/')
    contant = models.TextField()

    def __str__(self):
        return self.name

class AboutList(models.Model):
    about = models.ForeignKey(About, related_name='lists', on_delete=models.CASCADE)
    count = models.IntegerField()
    type1 = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.type1} ({self.count})"
