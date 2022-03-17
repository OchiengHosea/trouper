from django.db import models

from artist.models import Artist, ArtistR
from base.models import BaseModel, BaseModelIdOnly, BaseModelNoActive

class Album(BaseModelNoActive):
    name = models.CharField(max_length=255)

class Genre(BaseModelIdOnly):
    title = models.CharField(max_length=75)

class Song(BaseModel):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    file_url = models.CharField(max_length=215)
    file_name = models.CharField(max_length=215)
    # file_name = models.FileField(upload_to=f'songs/{artist.name}')
    
class SongRecognitionResult(BaseModelNoActive):
    artists = models.ManyToManyField(ArtistR)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    isrc = models.CharField(max_length=125)
    upc = models.CharField(max_length=125)
    bill_status = models.CharField(max_length=55, default='Pending')
    release_date = models.DateField()
    # record_time = models.DateTimeField()
    
    @property
    def artist_names(self):
        return "".join([artist.name for artist in self.artists])
    
    @property
    def genre_names(self):
        return "".join([genre.title for genre in self.genres])
    