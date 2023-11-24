from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название')
    author = models.CharField(max_length=50, verbose_name='Автор')
    publication_year = models.IntegerField(
        # Ограничиваем диапазон годов выпуска (числа из головы)
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(3000)
        ],
        verbose_name='Год издания'
    )
    isbn = models.CharField(max_length=17, verbose_name='Книжный номер')
