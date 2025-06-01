from django.db import models

class LandingPara(models.Model):
    p1 = models.TextField()

    def __str__(self):
        return self.p1[:50]  # First 50 characters


class ThemeSetting(models.Model):
    name = models.CharField(max_length=10, choices=[('light', 'Light'), ('dark', 'Dark')])
    colors = models.JSONField()
