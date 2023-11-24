from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, username
        and password.
        """

        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have an username.')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, username
        and password.
        """

        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)

        return user
