from rest_framework.response import Response
from rest_framework import generics,status
from .models import Order
from Menuapi.models import MenuItem
from .serializers import OrderSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class OrderView(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=OrderSerializer
    queryset=Order.objects.select_related('menuitem').all()
    def create(self,request):
        menuitems=request.data.get('menuitem')
        user=User.objects.get(username=self.request.user.username)
        time=""
        date=""
        for item in menuitems:
            menu=MenuItem.objects.get(item=item['item'],price=item['price'])
            order=Order.objects.create(menuitem=menu,total=request.data['total'],user=user)
            order.save()
            time=order.date.strftime("%H:%M:%S")
            date=order.date.date()
        return Response({"menuitem":menuitems,"time":time,"date":date})
