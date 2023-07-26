import os

from where_to_go.settings import MEDIA_ROOT
from places.models import Place, PlaceImage
from django.core.management.base import BaseCommand

import requests


class Command(BaseCommand):
    help = 'Adding more places from .json file to the map (in DB)\n' \
           'When downloading .json files from github, use strictly references to row.\n\n' \
           'For example: https://raw.githubusercontent.com/<USERNAME>/<PROJECT_NAME>/<BRANCH>/<PATH>'

    def add_arguments(self, parser):
        parser.add_argument('link_to_json', type=str, help='Link to .json file')

    def handle(self, *args, **options):
        response = requests.get(options['link_to_json'])
        response.raise_for_status()
        result = response.json()

        title = result['title']
        description_short = result['description_short']
        description_long = result['description_long']
        coordinates = result['coordinates']
        lng, lat = coordinates['lng'], coordinates['lat']
        imgs = result['imgs']

        place, is_added = Place.objects.get_or_create(title=title, lng=lng, lat=lat, defaults={
            'description_short': description_short,
            'description_long': description_long,
        })

        for i, img in enumerate(imgs, start=1):
            response = requests.get(img)
            response.raise_for_status()
            try:
                path_to_image = os.path.join(MEDIA_ROOT, (img.split('/')[-1]))
                with open(path_to_image, 'wb') as file:
                    file.write(response.content)
                image_object = PlaceImage(image=path_to_image, place=place, order=i)
                image_object.save()
            except Exception as e:
                print(f'Error while adding photos to DB: {e}')
        if is_added:
            print(f'{title} was successfully added!')
        else:
            print('Object already exist and was not rewrote!')
