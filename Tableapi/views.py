from rest_framework.response import Response
from rest_framework import status,generics
from .models import Table
from .serializers import tableserializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class tableview(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=tableserializer
    queryset=Table.objects.all()
    def post(self, request, format=None):
        serializer = tableserializer(data=request.data)

        if serializer.is_valid():
            # Set the user field to the current user before saving
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class edittableview(generics.DestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=tableserializer
    queryset=Table.objects.all()
