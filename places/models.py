from django.db import models
from tinymce.models import HTMLField


class PlaceImage(models.Model):
    description = models.CharField(max_length=200, verbose_name='Описание картинки')
    image = models.ImageField(verbose_name='Картинка')

    def __str__(self):
        return f'{self.pk} {self.description}'


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название локации', unique=True)
    imgs = models.ManyToManyField(PlaceImage, verbose_name='Картинки локации')
    description_short = models.TextField(null=True, blank=True, verbose_name='Короткое описание')
    description_long = HTMLField(null=True, blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    slug = models.CharField(max_length=200, verbose_name='Латинизированное название локации')
