from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.db import models


# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
        verbose_name='Почта',
        max_length=100,
    )
    phone_number = PhoneNumberField(unique=True, null=True, blank=True, verbose_name='Телефон')
    last_seen = models.DateTimeField(blank=True, null=True, verbose_name='Был в сети')
    is_blocked = models.BooleanField(default=False)

    REQUIRED_FIELDS = []

    @property
    def is_authenticated(self):
        return self.is_active
