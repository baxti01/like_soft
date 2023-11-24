from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from users.managers import MyUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True, verbose_name='Электронная почта')
    username = models.CharField(max_length=100, unique=True, verbose_name='Имя пользователя')

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    is_active = models.BooleanField(default=True, verbose_name='Статус')
    is_staff = models.BooleanField(default=False, verbose_name='is staff')
    is_superuser = models.BooleanField(default=False, verbose_name='is superuser')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return self.email
