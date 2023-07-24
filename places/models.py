from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название локации', unique=True)
    description_short = models.TextField(blank=True, verbose_name='Короткое описание')
    description_long = HTMLField(blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return f'{self.pk} | {self.title}'


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place, verbose_name='Локация', on_delete=models.SET_NULL, null=True,
                              related_query_name='images', related_name='image')
    order = models.PositiveIntegerField('Позиция', default=0)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        ordering = ['order']
