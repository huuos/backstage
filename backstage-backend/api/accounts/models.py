from django.db import models

# Create your models here.
class Account(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)