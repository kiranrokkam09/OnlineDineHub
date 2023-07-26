from rest_framework.response import Response
from rest_framework import generics,status
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
