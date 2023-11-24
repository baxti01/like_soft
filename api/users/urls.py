from django.urls import path, include

from api.users.views import UserView, UserCreateView

urlpatterns = [
    path('me/', UserView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('session/auth/', include('rest_framework.urls'))
]
