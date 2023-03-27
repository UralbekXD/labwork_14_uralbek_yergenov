from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        null=False,
        blank=False,
        to=get_user_model(),
        related_name='posts',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    images = models.ImageField(
        null=False,
        blank=False,
        upload_to='posts',
        verbose_name='Картинки'
    )

    description = models.TextField(
        null=False,
        blank=False,
        max_length=256,
        verbose_name='Описание'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.author} {self.description[:20]}'
