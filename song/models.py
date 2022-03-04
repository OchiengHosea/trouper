from django.db import models

from artist.models import Artist
from base.models import BaseModel, BaseModelIdOnly

# Create your models here.

class Genre(BaseModelIdOnly):
    title = models.CharField(max_length=75)

class Song(BaseModel):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    file_name = models.FileField(upload_to=f'songs/{artist.name}')