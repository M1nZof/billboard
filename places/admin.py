from django.contrib import admin

from places.models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = Place.imgs.through


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [PlaceImageInline, ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description')
