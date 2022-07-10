from django.db import models
from levels.models import Level

# Create your models here.
class Enemy(models.Model):
    level = models.ManyToManyField(Level, related_name='enemy', blank=True)
    name = models.CharField(max_length=255, verbose_name='Имя врага')
    description = models.TextField(verbose_name='Описание врага')
    hp = models.IntegerField(verbose_name='Здоровье врага')
    power = models.IntegerField(verbose_name='Сила вражеской атаки')
    difficulty = models.CharField(max_length=255,verbose_name='Сложность вражеских атак')
    reward = models.IntegerField(verbose_name='Награда за убийство')
    image = models.ImageField(upload_to='enemies/images', verbose_name='Портрет врага')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Враг'
        verbose_name_plural = 'Враги'
