from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length = 50)
    anons = models.CharField('Анонс', max_length = 250)
    kategor = models.CharField('Категория', max_length = 50)
    prod = models.TextField('Продукты')
    full_text = models.TextField('Рецепт приготовления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/recipes/{self.id}'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'