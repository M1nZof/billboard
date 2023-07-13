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
        if response.reason == 'OK':
            result = response.json()
            title, description_short, description_long, coordinates = result['title'], result['description_short'], \
                                                                      result['description_long'], result['coordinates']
            lng, lat = coordinates['lng'], coordinates['lat']
            imgs = result['imgs']

            place, is_added = Place.objects.get_or_create(title=title, description_short=description_short,
                                                          description_long=description_long, lng=lng, lat=lat, slug='')

            for img in imgs:
                response = requests.get(img)
                if response.reason == 'OK':
                    try:
                        path_to_image = os.path.join(MEDIA_ROOT, (img.split('/')[-1]))
                        with open(path_to_image, 'wb') as file:
                            file.write(response.content)
                        image_object = PlaceImage(description=title)
                        image_object.image = path_to_image
                        image_object.save()
                        place.imgs.add(image_object)
                    except Exception as e:
                        print(f'Error while adding photos to DB: {e}')
                else:
                    print(f'{title} | some error while downloading photos')
                    break
            if is_added:
                print(f'{title} was successfully added!')
            else:
                print('Object already exist and was not rewrote!')
        else:
            print(f'Something went wrong. {response.status_code}: {response.reason}')
