# Generated by Django 4.0.1 on 2023-03-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likedislike', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedislike',
            name='is_dislike',
            field=models.BooleanField(default=False, unique=True),
        ),
        migrations.AlterField(
            model_name='likedislike',
            name='is_like',
            field=models.BooleanField(default=False, unique=True),
        ),
    ]
