from rest_framework import serializers
from bookswap.models.book_models import Book

class BookSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'is_available', 'created_at', 'owner_name']

    def get_owner_name(self, obj):
        return f"{obj.owner.first_name} {obj.owner.last_name}"
