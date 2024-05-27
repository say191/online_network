from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for product's views"""
    class Meta:
        model = Product
        fields = '__all__'
