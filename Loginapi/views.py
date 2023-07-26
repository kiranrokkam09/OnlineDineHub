from rest_framework import generics,status
from django.contrib.auth.models import User
from .serializers import userserializer
from rest_framework.response import Response
from django.contrib.auth import login,logout,authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
# Create your views here.

class registerview(generics.CreateAPIView):
    serializer_class=userserializer
    queryset=User.objects.all()

class logoutview(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response({"message":"Logout Successful"})

