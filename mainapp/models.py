from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=256)
    image = models.ImageField(upload_to='products_image', blank=True)
    short_description = models.CharField(verbose_name='краткое описание продуктв', max_length=64, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.name} ({self.category.name})"
