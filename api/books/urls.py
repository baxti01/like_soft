from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.books.views import BookModelViewSet

router = SimpleRouter()

router.register('', BookModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
