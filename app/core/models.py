from django.db import models

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.mixins import PermissionRequiredMixin
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

    def create_superuser(self, email, last_name, birth_date, first_name=None,  password=None):
        superuser = self.create_user(email, first_name, last_name, birth_date,
                                     password=password, is_active=True, is_coach=True, is_admin=True)
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






#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=100)
#     city_address = models.CharField(max_length=100)
#     street_address = models.CharField(max_length=100)
#     birth_date = models.DateField(null=True)
#     is_active = models.BooleanField()
#     is_coach = models.BooleanField()
#     is_admin = models.BooleanField()
#     join_date = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#







#
#
#
#
#
#
# class MemberManager(BaseUserManager):
#     def create_user(self, email, first_name, last_name, birth_date, password=None, is_active=False, is_coach=False, is_admin=False):
#         if not email:
#             raise ValueError("User must have Email address")
#         if not password:
#             raise ValueError("User must have Password")
#         if not first_name:
#             raise ValueError("User must have First name")
#         if not last_name:
#             raise ValueError("User must have Last name")
#         if not birth_date:
#             raise ValueError("User must have birth date")
#
#         user_obj = self.model(
#             email=self.normalize_email(email)
#         )
#         user_obj.set_password(password)
#         user_obj.first_name = first_name
#         user_obj.last_name = last_name
#         user_obj.birth_date = birth_date
#         user_obj.is_active = is_active
#         user_obj.is_admin = is_admin
#         user_obj.is_coach = is_coach
#         user_obj.save(using=self._db)
#         return user_obj
#
#     def create_coach(self, email, first_name, last_name, birth_date, password=None):
#         coach = self.create_user(email, first_name, last_name,
#                                  birth_date, password=password, is_active=True, is_coach=True)
#         return coach
#
#     def create_superuser(self, email, last_name, birth_date, first_name=None,  password=None):
#         superuser = self.create_user(email, first_name, last_name, birth_date,
#                                      password=password, is_active=True, is_coach=True, is_admin=True)
#         return superuser
#
#
#
#
#
#
#
#
#
# class Member(AbstractBaseUser, PermissionsMixin):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=100)
#     city_address = models.CharField(max_length=100)
#     street_address = models.CharField(max_length=100)
#     birth_date = models.DateField(null=True)
#     is_active = models.BooleanField()
#     is_coach = models.BooleanField()
#     is_admin = models.BooleanField()
#     join_date = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#
#     objects = MemberManager()
#
#     def __str__(self):
#         return self.email
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     @property
#     def is_staff(self):
#         return True
#
#     @property
#     def is_superuser(self):
#         return self.is_admin
