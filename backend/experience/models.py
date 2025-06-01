from django.db import models

class Experience(models.Model):
    duration = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.role}"
