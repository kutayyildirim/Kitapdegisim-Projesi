from rest_framework import serializers
from bookswap.models.user_models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'city']
