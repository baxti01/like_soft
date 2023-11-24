from rest_framework.viewsets import ModelViewSet

from api.books.serializers import BookModelSerializer
from apps.books.models import Book


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
