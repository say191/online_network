from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user's views"""
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'fio', 'phone', 'is_active']
