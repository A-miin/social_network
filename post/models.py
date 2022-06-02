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
        _('Author'),
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts',
    )
    like = models.ManyToManyField(
        _('Like'),
        get_user_model(),
        related_name='liked_posts',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title
