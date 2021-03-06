from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Create your models here.


class Post(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=128,
    )
    description = models.CharField(
        _('Description'),
        max_length=2024,
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        get_user_model(),
        verbose_name=_('Author'),
        on_delete=models.CASCADE,
        related_name='posts',
    )
    like = models.ManyToManyField(
        get_user_model(),
        verbose_name=_('Like'),
        related_name='liked_posts',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return f'{self.id}. {self.title}'
