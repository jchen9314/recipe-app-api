from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
                                        PermissionMixin
                                    

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password) # encrypt password
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BoobleanField(default=False)

    objects = UserManager()
     