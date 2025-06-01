from django.db import models

class EducationGroup(models.Model):
    heading = models.CharField(max_length=100)

    def __str__(self):
        return self.heading

class EducationItem(models.Model):
    group = models.ForeignKey(EducationGroup, related_name='one', on_delete=models.CASCADE)
    passedout = models.CharField(max_length=20)
    institute = models.CharField(max_length=100)
    locations = models.CharField(max_length=100)
    sub = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sub} - {self.institute} ({self.passedout})"
