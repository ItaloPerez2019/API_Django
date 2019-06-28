from django.db import models
# Create your models here.

class Expense(models.Model):
#ID, description, amount , type , date
    description = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    types = models.CharField(max_length=100)
    date =models.DateField(auto_now=False, auto_now_add=False)

