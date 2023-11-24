from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from api.users.serializers import UserModelSerializer, UserCreateSerializer
from api.users.tasks import send_email_task

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        send_email_task.delay(username=user.username, email=user.email)


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_object(self):
        return self.request.user
