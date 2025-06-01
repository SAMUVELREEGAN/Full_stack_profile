from django.db import models

class Detail(models.Model):
    mynamebefore = models.CharField(max_length=100)
    mynamebeAfter = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    detailcontant = models.TextField()
    mypic1 = models.ImageField(upload_to='detail_images/')
    mypic2 = models.ImageField(upload_to='detail_images/')

    def __str__(self):
        return f"{self.mynamebefore}{self.mynamebeAfter}"
