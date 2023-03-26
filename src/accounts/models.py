from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Account(AbstractUser):
    class Genders(models.TextChoices):
        MALE = 'male', 'Мужчина'
        FEMALE = 'female', 'Женщина'

    # Required
    email = models.EmailField(
        verbose_name='Почта',
        unique=True,
        null=False,
        blank=False,
    )

    # Required
    avatar = models.ImageField(
        null=False,
        blank=False,
        upload_to='avatars',
        verbose_name='Аватар'
    )

    about = models.TextField(
        max_length=2048,
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    phone_number = PhoneNumberField(
        null=True,
        blank=True,
        unique=True,
        verbose_name='Номер телефона'
    )

    gender = models.CharField(
        max_length=6,
        choices=Genders.choices,
        null=True,
        blank=True,
        verbose_name='Пол'
    )

    following = models.ManyToManyField(
        verbose_name='Подписчики',
        to='accounts.Account',
        related_name='followers',
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
