# Generated by Django 4.2.1 on 2023-05-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeimage',
            name='description',
            field=models.CharField(default='image', max_length=200, verbose_name='Описание картинки'),
            preserve_default=False,
        ),
    ]
