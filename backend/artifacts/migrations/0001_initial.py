# Generated by Django 4.0.5 on 2022-06-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('levels', '0004_alter_level_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название артефакта')),
                ('description', models.TextField(verbose_name='Описание артефакта')),
                ('rarity', models.CharField(max_length=255, verbose_name='Редкость артефакта')),
                ('image', models.ImageField(upload_to='artifacts/images', verbose_name='Иллюстрация артефакта')),
                ('level', models.ManyToManyField(blank=True, related_name='artifact', to='levels.level')),
            ],
            options={
                'verbose_name': 'Артефакт',
                'verbose_name_plural': 'Артефакты',
            },
        ),
    ]
