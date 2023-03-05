from django.db import models

# Create your models here.
class message(models.Model):
    username = models.TextField(max_length=50,null=True)
    email = models.EmailField(max_length=100, null=True)
    subject = models.TextField(max_length=200, null=True)
    msg = models.TextField(max_length=1000, null=True)
