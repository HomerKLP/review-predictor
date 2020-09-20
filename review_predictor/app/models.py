# Vendor
from django.db import models


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    text = models.TextField('Отзыв')
    rating = models.PositiveSmallIntegerField('Рейтинг', db_index=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
