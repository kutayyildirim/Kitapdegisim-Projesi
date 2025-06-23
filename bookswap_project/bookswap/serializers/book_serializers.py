from rest_framework import serializers
from bookswap.models.book_models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
