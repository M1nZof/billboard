from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 0

    fields = ['show_image', ]
    readonly_fields = ['show_image']

    def show_image(self, obj):
        image_object = PlaceImage.objects.filter(pk=obj.placeimage_id).first()
        return format_html(f'<img src="{image_object.image.url}" height="200">')
    show_image.short_description = 'Фотографии'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline, ]
    list_display = ('title', )


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('pk', )
