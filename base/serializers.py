from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from artist.models import ArtistR

from song.models import Genre, SongRecognitionResult

class ArtistRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistR
        fields = ('name',)
        
class GenreRSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('title',)
class RecognitionResultSerializer(serializers.ModelSerializer):
    artists = ArtistRSerializer
    class Meta:
        model = SongRecognitionResult
        fields = '__all__'