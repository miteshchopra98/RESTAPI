from rest_framework import serializers
from products.models import *

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Products
        fields = ['id', 'title', 'content', 'price', 'sale_price', 'my_discount']


    def get_my_discount(self, obj):
        return obj.get_discount() + 5