# Generated by Django 4.2.1 on 2023-06-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_place_imgs'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.CharField(default='asd', max_length=200, verbose_name='Латинизированное название локации'),
            preserve_default=False,
        ),
    ]