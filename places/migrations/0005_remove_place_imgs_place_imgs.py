# Generated by Django 4.2.1 on 2023-06-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_place_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='imgs',
        ),
        migrations.AddField(
            model_name='place',
            name='imgs',
            field=models.ManyToManyField(null=True, to='places.placeimage', verbose_name='Картинки локации'),
        ),
    ]
