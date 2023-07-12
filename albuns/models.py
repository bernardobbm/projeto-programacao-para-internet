from django.db import models

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    genrer = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, related_name='album_artist')
    release_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to= 'albuns/', blank=True, null=True)

    def __str__(self):
        return self.genrer
