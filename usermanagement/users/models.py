from django.db import models

class User(models.Model):

    class Meta:
        db_table = 'users'

    id = models.AutoField(primary_key=True) # default
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

