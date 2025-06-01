from django.db import models

class ProjectURl(models.Model):
    pro_name = models.CharField(max_length=255)
    pro_url = models.URLField()

    def __str__(self):
        return self.pro_name
