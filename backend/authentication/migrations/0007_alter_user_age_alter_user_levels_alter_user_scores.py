# Generated by Django 4.0.5 on 2022-06-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='levels',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='scores',
            field=models.IntegerField(),
        ),
    ]
