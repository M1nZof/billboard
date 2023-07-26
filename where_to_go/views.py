from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
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
        features.append(place_properties)
    rendered_places = {
        'data':
            {
                "type": "FeatureCollection",
                "features": features
            }
    }

    return render(request, 'index.html', context=rendered_places)


def place_page(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return JsonResponse(serialize_place(place))


def serialize_place(place):
    return {
        'title': place.title,
        'imgs': [place.image.url for place in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
