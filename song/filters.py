from dataclasses import fields
import django_filters

from song.models import SongRecognitionResult

class RecognitionResultFilter(django_filters.FilterSet):
    played_by = django_filters.CharFilter(field_name='recorded_by__name', lookup_expr='icontains')
    recognition_date_from = django_filters.DateTimeFilter(field_name='created_on', lookup_expr='gte')
    recognition_date_to = django_filters.DateTimeFilter(field_name='created_on', lookup_expr='lte')
    artist = django_filters.CharFilter(field_name='artists', lookup_expr='icontains')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    
    class Meta:
        fields = [
            'played_by', 
            'recognition_date_start',
            'recognitino_date_end',
            'artist',
            'title'
            ]
        