from rest_framework import serializers
from .models import Table
from django.core.validators import MinValueValidator

class tableserializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields="__all__"
        extra_kwargs={
            'guests':{'max_value':6,'min_value':1},
        }
