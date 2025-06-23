from rest_framework import viewsets
from bookswap.models.user_models import User
from bookswap.serializers.user_serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
