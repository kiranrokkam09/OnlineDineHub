from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Table(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    guests=models.IntegerField(null=False,blank=False)
    time=models.TimeField(null=False,blank=False)
    date=models.DateField(null=False,blank=False)
