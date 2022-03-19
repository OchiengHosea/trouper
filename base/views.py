import imp
from os import link
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from base.serializers import RecognitionResultSerializer

from django.db import transaction

from artist.models import Artist, ArtistR
from song.filters import RecognitionResultFilter
from song.models import Album, Genre, Recorder, SongRecognitionResult
from django.db.models import Count
# Create your views here.
class HomePage(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        key_features = [
                dict(title='Artists', caption="Major and upcoming artists", link='artist:artist_list', skin='artist'),
                dict(title='Songs', caption="Curated top hits", link='song:song_list', skin='song'),
                dict(title='Albums', caption="Straight from how 'twas made", link='song:song_list', skin='music')
            ]
        data = dict(
            key_features=key_features
        )
        context.update(data)
        return context
    
    
class MusicResultAPIView(APIView):
    def post(self, *args, **kwargs):
        print("Post Data: ", self.request.POST)
        print("Params Data: ", self.request.GET)
        return Response('data received', status=status.HTTP_200_OK)
    
class RecognitionResultsAPIView(APIView):
    @transaction.atomic
    def post(self, *args, **kwargs):
        music_data = self.request.data
        artists_list = music_data["artists"]
        artists = [ArtistR.objects.create(name=artist['name']) for artist in artists_list]
        
        album = Album.objects.create(name=music_data['album']['name'])
                
        genres_list = music_data["genres"]
        
        genres = [Genre.objects.create(title=genre['name']) for genre in genres_list]
        
        title = music_data["title"]
        label = music_data["label"]

        external_ids = music_data["external_ids"]
        release_date = datetime.strptime(music_data["release_date"], '%Y-%m-%d').date()
        # record_time = datetime.strptime(music_data["timestamp_utc"], '%Y-%m-%d %H:%m:%S')
        try:
            isrc = external_ids['isrc'][0]
            upc = external_ids['upc'][0]
            entry = SongRecognitionResult.objects.create(
                title=title, 
                label=label, 
                album=album, 
                iscr=isrc, 
                upc=upc, 
                release_date=release_date)
        except Exception as e:
            isrc = external_ids['isrc']
            upc = external_ids['upc']
            entry = SongRecognitionResult.objects.create(
                title=title,
                label=label,
                album=album,
                isrc=isrc,
                upc=upc,
                release_date=release_date)
        
        [entry.artists.add(artist) for artist in artists]
        [entry.genres.add(genre) for genre in genres]
        
        return Response('Entry made successfully', status=status.HTTP_200_OK)
    
class RecognitionResultsList(ListAPIView):
    model = SongRecognitionResult
    serializer_class = RecognitionResultSerializer
    
    def get_queryset(self):
        return self.model.objects.all()
    
class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recorders"] = Recorder.objects.all()
        return context
    
class RecognitionResultsSummary(TemplateView):
    template_name = 'song/recognition_results.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        results = RecognitionResultFilter(self.request.GET, queryset=SongRecognitionResult.objects.all())
        
        summary = results.qs \
            .values('title', 'label', 'isrc', 'upc') \
            .annotate(frequency=Count('isrc')) \
            .order_by('-frequency')
            
        context.update(dict(summaries=summary))
        return context



class RecognitionResultsSummaryAPIView(APIView):
    def get(self, *args, **kwargs):
        summary = SongRecognitionResult.objects.all() \
            .values('title', 'label', 'isrc', 'upc') \
            .annotate(frequency=Count('title')) \
            .order_by('-frequency')
            
        return Response(summary, status=status.HTTP_200_OK)
    