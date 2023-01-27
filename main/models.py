from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=100)
