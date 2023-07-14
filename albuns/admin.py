from django.contrib import admin
from albuns.models import Album, Artist

# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'country')
    search_fields = ('name',)

admin.site.register(Artist, ArtistAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('genrer', 'name', 'artist', 'release_year', 'number_of_sales')
    search_fields = ('genrer', 'artist')

#registrar
admin.site.register(Album, AlbumAdmin)