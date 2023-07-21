from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название локации', unique=True)
    description_short = models.TextField(null=True, blank=True, verbose_name='Короткое описание')
    description_long = HTMLField(null=True, blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return f'{self.pk} | {self.title}'


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place, verbose_name='Локация', on_delete=models.SET_NULL, null=True,
                              related_query_name='images', related_name='image')

    def __str__(self):
        return f'{self.pk}'
