# Generated by Django 4.1.5 on 2023-09-22 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlesson',
            name='last_viewed_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Последний раз просмотрено'),
        ),
        migrations.AlterField(
            model_name='productuser',
            name='access',
            field=models.BooleanField(default=False, verbose_name='Есть ли доступ'),
        ),
        migrations.AlterField(
            model_name='productuser',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_user', to=settings.AUTH_USER_MODEL, verbose_name='Владелец продукта'),
        ),
        migrations.AlterField(
            model_name='productuser',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='userlesson',
            name='is_viewed',
            field=models.BooleanField(default=False, verbose_name='Просмотрено ли'),
        ),
        migrations.AlterField(
            model_name='userlesson',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_lesson', to='products.lesson', verbose_name='Урок'),
        ),
        migrations.AlterField(
            model_name='userlesson',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='userlesson',
            name='viewed_time',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Просмотренное время'),
        ),
        migrations.AddConstraint(
            model_name='productuser',
            constraint=models.UniqueConstraint(fields=('owner', 'product'), name='unique_product_owner'),
        ),
        migrations.AddConstraint(
            model_name='userlesson',
            constraint=models.UniqueConstraint(fields=('user', 'lesson'), name='unique_user_lesson'),
        ),
    ]