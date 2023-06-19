from django.db import models


class PlaceImage(models.Model):
    description = models.CharField(max_length=200, verbose_name='Описание картинки')
    image = models.ImageField(verbose_name='Картинка')


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название локации')
    imgs = models.ForeignKey(PlaceImage, on_delete=models.SET_NULL, null=True, verbose_name='Картинки локации')
    description_short = models.CharField(max_length=200, verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    slug = models.CharField(max_length=200, verbose_name='Латинизированное название локации')
