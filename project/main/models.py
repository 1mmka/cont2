from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=64, verbose_name='Имя пользователя')
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'