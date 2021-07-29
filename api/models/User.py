
from django.contrib.auth.models import AbstractUser
from django.db import models
from .Phones import Phones


class User(AbstractUser):
    id = models.AutoField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    phones = models.ManyToManyField(Phones, null=True, blank=True, related_name='user_phones')
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
