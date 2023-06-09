# Generated by Django 4.1.7 on 2023-03-22 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=False)),
                ('is_dislike', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_received', to=settings.AUTH_USER_MODEL, verbose_name='user_id - На кого поставили лайк/дизлайк')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_sent', to=settings.AUTH_USER_MODEL, verbose_name='user_id - Кто поставил лайк/дизлайк')),
            ],
            options={
                'verbose_name': 'Лайк-Дизлайк',
            },
        ),
    ]
