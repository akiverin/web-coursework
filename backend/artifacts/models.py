from django.db import models
from levels.models import Level

# Create your models here.
class Artifact(models.Model):
    level = models.ManyToManyField(Level, related_name='artifact', blank=True)
    name = models.CharField(max_length=255, verbose_name='Название артефакта')
    description = models.TextField(verbose_name='Описание артефакта')
    rarity = models.CharField(max_length=255,verbose_name='Редкость артефакта')
    image = models.ImageField(upload_to='artifacts/images', verbose_name='Иллюстрация артефакта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Артефакт'
        verbose_name_plural = 'Артефакты'
