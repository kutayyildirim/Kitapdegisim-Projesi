from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from bookswap.models.book_models import Book
from bookswap.serializers.book_serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['is_available', 'author']
    search_fields = ['title', 'author']
    ordering_fields = ['created_at', 'title']