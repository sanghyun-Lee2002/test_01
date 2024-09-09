from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=15)
    nicname = models.CharField(max_length=20)
    birthday = models.DateField()

    gender = models.CharField(blank=True, max_length=2)
    memo = models.TextField(blank=True)
