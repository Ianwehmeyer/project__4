from django.db import models

# Create your models here.
class Account( models.Model):
    total = models.IntegerField();

class Things( models.Model):
    amount = models.IntegerField();
    name = models.CharField( max_length=30)