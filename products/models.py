from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint

User = get_user_model()


class Product(models.Model):
    name = models.CharField(
        verbose_name='Название продукта',
        max_length=50
    )
    description = models.TextField(
        verbose_name='Описание продукта',
        max_length=255
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Lesson(models.Model):
    name = models.CharField(
        verbose_name='Название урока',
        max_length=50
    )
    link = models.URLField(
        verbose_name='Ссылка на урок',
        max_length=255
    )
    duration = models.PositiveIntegerField(
        verbose_name='Длительность в секундах'
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Продукт',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class ProductUser(models.Model):
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец продукта',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Продукт',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    access = models.BooleanField(
        verbose_name='Есть ли доступ',
        default=False
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'продукт пользователя'
        verbose_name_plural = 'продукты пользователя'
        constraints = [
            UniqueConstraint(fields=['owner', 'product'], name='unique_product_owner')
        ]


class UserLesson(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    lesson = models.ForeignKey(
        Lesson,
        verbose_name='Урок',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    viewed_time = models.PositiveIntegerField(
        verbose_name='Просмотренное время',
        null=True,
        blank=True
    )
    is_viewed = models.BooleanField(
        verbose_name='Просмотрено ли',
        default=False
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'урок в продукте'
        verbose_name_plural = 'уроки в продукте'
        constraints = [
            UniqueConstraint(fields=['user', 'lesson'], name='unique_user_lesson')
        ]
