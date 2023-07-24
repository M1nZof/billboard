from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def index(request):
    places = Place.objects.all()
    rendered_places = {
        'data':
            {
                "type": "FeatureCollection",
                "features": []
            }
    }
    for counter, place in enumerate(places):
        place_properties = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.pk,
                'detailsUrl': reverse('places', args=(place.pk, ))
            }
        }
        rendered_places['data']['features'].append(place_properties)

    return render(request, 'index.html', context=rendered_places)


def place_page(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return JsonResponse(serialize_place(place))


def serialize_place(place):
    return {
        'title': place.title,
        'imgs': [place.image.url for place in place.image.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
