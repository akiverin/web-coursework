# Generated by Django 4.0.5 on 2022-06-19 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_user_age_alter_user_levels_alter_user_scores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Возраст пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='diamonds',
            field=models.IntegerField(default=0, verbose_name='Внутриигровая валюта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='levels',
            field=models.IntegerField(default=0, verbose_name='Количество пройденных уровней'),
        ),
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.IntegerField(default=0, verbose_name='Внутриигровая валюта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='scores',
            field=models.IntegerField(default=0, verbose_name='Набранные очки пользователем'),
        ),
    ]
