from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authentication.managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=64, verbose_name='Имя пользователя', unique=True)
    email = models.EmailField(max_length=255, verbose_name='Email адрес')
    image = models.ImageField(upload_to='users/images', verbose_name='Аватар пользователя',default='users/images/KnightAvatar.jpeg')
    type = models.CharField(max_length=64, verbose_name='Тип аккаунта', default='player')
    age = models.IntegerField(verbose_name='Возраст пользователя', default=0)
    levels = models.IntegerField(verbose_name='Количество пройденных уровней', default=0)
    scores = models.IntegerField(verbose_name='Набранные очки пользователем', default=0)
    money = models.IntegerField(verbose_name='Внутриигровая валюта Монеты', default=0)
    diamonds = models.IntegerField(verbose_name='Внутриигровая валюта Алмазы', default=0)

    is_activ = models.BooleanField(default=True, verbose_name='Активен')
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    is_superuser = models.BooleanField(default=False, verbose_name='Администратор')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
