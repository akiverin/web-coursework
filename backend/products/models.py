from django.db import models
from authentication.models import User

# Create your models here.
class Product(models.Model):
    user = models.ManyToManyField(User, related_name='user', blank=True)
    name = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.IntegerField(verbose_name='Цена товара')
    image = models.ImageField(upload_to='products/images', verbose_name='Иллюстрация товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
