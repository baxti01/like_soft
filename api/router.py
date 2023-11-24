from django.urls import path, include

urlpatterns = [
    path('books/', include('api.books.urls')),
    path('users/', include('api.users.urls')),

    # OpenApi docs
    path('openapi/', include('api.openapi.urls')),
]
