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
        blank=True,
        to='accounts.Account',
        verbose_name='Подписчики',
        related_name='followers',
    )

    liked_posts = models.ManyToManyField(
        blank=True,
        to='posts.Post',
        related_name='liked_users',
        verbose_name='Понравившиеся публикации',
    )

    commented_posts = models.ManyToManyField(
        blank=True,
        to='posts.Post',
        related_name='commented_users',
        verbose_name='Прокомментированные публикации',
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
