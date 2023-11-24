from rest_framework import serializers

from apps.books.models import Book


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'name',
            'author',
            'publication_year',
            'isbn'
        ]
