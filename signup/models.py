from django.db import models

class Signup(models.Model):
    username = models.TextField(max_length=16)
    email = models.TextField(max_length=50)
    password = models.TextField(max_length=16)
    account_type = models.TextField(max_length=6)
