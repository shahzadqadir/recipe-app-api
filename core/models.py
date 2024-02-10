from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):

    def create_user(self, password, email):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("An email must be provided.")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def normalize_email(self, email):
        return email.lower()

    def create_superuser(self, email, password):
        """Create a super user"""
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(PermissionsMixin, AbstractBaseUser):
    """Custom User model that supports user email instead of username"""
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
