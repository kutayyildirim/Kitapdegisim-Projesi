from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from bookswap.models.user_models import User
from bookswap.serializers.user_serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['city']
    search_fields = ['username', 'email', 'first_name', 'last_name']

