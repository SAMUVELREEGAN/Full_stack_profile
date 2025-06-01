from django.db import models

class MyContact(models.Model):
    phone = models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField()
    mypdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return f"{self.email}"
    


class AutoReplyMessage(models.Model):
    FORM_TYPE_CHOICES = [
        ('connect', 'Connect'),
        ('hiring', 'Hiring'),
        ('freelance', 'Freelance'),
    ]

    form_type = models.CharField(max_length=20, choices=FORM_TYPE_CHOICES, unique=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.get_form_type_display()} Auto-Reply"
