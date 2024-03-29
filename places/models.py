from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название локации', unique=True)
    description_short = models.TextField(blank=True, verbose_name='Короткое описание')
    description_long = HTMLField(blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return f'ID: {self.pk} | Локация: {self.title}'


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place, verbose_name='Локация', on_delete=models.CASCADE,
                              related_name='images', related_query_name='image')
    order = models.PositiveIntegerField('Позиция', default=0, blank=True)

    def __str__(self):
        return f'ID: {self.pk} | Локация: {self.place.title}'

    class Meta:
        ordering = ['order']
