from django.contrib import admin

from places.models import Place, PlaceImage


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', )


class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description')


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage, PlaceImageAdmin)

