from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, last_name, birth_date,
                         first_name=None,  password=None):
        superuser = self.create_user(email, first_name, last_name, birth_date,
                                     password=password, is_active=True,
                                     is_coach=True, is_admin=True)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # put a field as a default username field if it doesn't exist
    USERNAME_FIELD = "email"

    @property
    def is_superuser(self):
        return self.is_admin
