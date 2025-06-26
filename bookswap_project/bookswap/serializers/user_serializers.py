from rest_framework import serializers
from bookswap.models.user_models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'city']

    def validate_first_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("İsim boş bırakılamaz.")
        return value

    def validate_last_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Soyisim boş bırakılamaz.")
        return value
