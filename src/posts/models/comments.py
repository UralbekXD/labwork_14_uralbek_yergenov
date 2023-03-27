from django.contrib.auth import get_user_model
from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(
        null=False,
        blank=False,
        to=get_user_model(),
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    post = models.ForeignKey(
        null=False,
        blank=False,
        to='posts.Post',
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )

    text = models.TextField(
        null=False,
        blank=False,
        max_length=256,
        verbose_name='Комментарий'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.author} {self.post} {self.text[:20]}'
