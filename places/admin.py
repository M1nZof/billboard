from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, PlaceImage


class PlaceImageInline(SortableStackedInline):
    model = PlaceImage
    extra = 0

    readonly_fields = ['show_image']

    def show_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" height="200">')
    show_image.short_description = 'Превью картинки'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PlaceImageInline, ]
    list_display = ('title', 'description_short')


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'place')
