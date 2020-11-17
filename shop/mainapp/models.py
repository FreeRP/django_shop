from django.db import models

class Category(models.Model):

    slug = models.CharField(max_length=100, verbose_name='slug')
    name = models.CharField(max_length=100, verbose_name='название категории')
    image_name = models.CharField(max_length=100, verbose_name='название изображения')
    clothes = models.ForeignKey('Clothes', blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Clothes(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='цена')
    img_name = models.CharField(max_length=100, verbose_name='название изображения')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'clothes'
