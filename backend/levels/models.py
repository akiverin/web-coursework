from django.db import models
from authentication.models import User

# Create your models here.
class Level(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название уровня')
    description = models.TextField(verbose_name='Описание уровня')
    difficulty = models.CharField(max_length=255,verbose_name='Сложность уровня')
    reward = models.IntegerField(verbose_name='Награда за прохождение уровня')
    best_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='best_levels')
    image = models.ImageField(upload_to='levels/images', verbose_name='Пейзаж уровня')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'
