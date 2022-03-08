from django.urls import path
import song.views as song_views

urlpatterns = [
    path('', song_views.SongListView.as_view(), name='song_list'),
    path('publish_song', song_views.SongCreateView.as_view(), name='publish_song'),
]
