from django.db import models
from levels.models import Level

# Create your models here.
class Achievement(models.Model):
    level = models.ManyToManyField(Level, related_name='achievement', blank=True)
    name = models.CharField(max_length=255, verbose_name='Названия достижения')
    description = models.TextField(verbose_name='Описание достижения')
    diamonds = models.IntegerField(verbose_name='Награда за достижение')
    image = models.ImageField(upload_to='achievements/images', verbose_name='Иллюстрация достижения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'
