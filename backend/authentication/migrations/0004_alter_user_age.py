# Generated by Django 4.0.5 on 2022-06-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(verbose_name='Возраст пользователя'),
        ),
    ]