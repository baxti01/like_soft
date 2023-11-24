from django.urls import path, include

urlpatterns = [
    path('books/', include('api.books.urls')),
    path('users/', include('api.users.urls'))
]
