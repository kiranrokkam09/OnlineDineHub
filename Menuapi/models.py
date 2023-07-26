from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MenuItem(models.Model):
    item=models.CharField(max_length=255,null=False,blank=False)
    price=models.DecimalField(max_digits=6,decimal_places=2,null=False,blank=False)
