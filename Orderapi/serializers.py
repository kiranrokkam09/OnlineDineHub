from rest_framework import serializers
from .models import Order
from Menuapi.serializers import MenuItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    menuitem=MenuItemSerializer(many=True)
    class Meta:
        model=Order
        fields="__all__"

    def __init__(self, *args, **kwargs):
        # Get the context to check if it's a POST request
        context = kwargs.get('context', {})
        is_post_request = context.get('request').method == 'POST'
        
        # Adjust the many parameter for menuitem based on the request method
        if is_post_request:
            self.fields['menuitem'] = MenuItemSerializer(many=True)
        else:
            self.fields['menuitem'] = MenuItemSerializer(many=False)

        super(OrderSerializer, self).__init__(*args, **kwargs)