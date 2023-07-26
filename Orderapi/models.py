from django.db import models
from Menuapi.models import MenuItem
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    menuitem=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    total=models.DecimalField(max_digits=6,decimal_places=2,null=False,blank=False)
    