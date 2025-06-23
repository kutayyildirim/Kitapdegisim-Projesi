from rest_framework import viewsets
from bookswap.models.book_models import Book
from bookswap.serializers.book_serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
