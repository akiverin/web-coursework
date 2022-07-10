# Generated by Django 4.0.5 on 2022-06-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=18, verbose_name='Возраст пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_activ',
            field=models.BooleanField(default=False, verbose_name='Активен'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Персонал'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Администратор'),
        ),
    ]
