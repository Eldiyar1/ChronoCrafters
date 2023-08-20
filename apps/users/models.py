from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .managers import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['firstname', 'lastname']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/avatars/', blank=True, null=True, verbose_name='Profiles_avatar',)
    email = models.EmailField(null=True, verbose_name='Email')
    phone_number = PhoneNumberField(null=True, verbose_name='Номер телефона',)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.email