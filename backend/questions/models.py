from django.db import models

class Question(models.Model):
    qus = models.TextField()
    ans = models.TextField()

    def __str__(self):
        return self.qus[:50]  # Show first 50 chars in admin
