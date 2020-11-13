from django.db import models


class Clothes(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='цена')
    img_name = models.CharField(max_length=100, verbose_name='название изображения')

    def __str__(self):
        return self.name
