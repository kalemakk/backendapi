from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.EmailField(max_length=20)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
