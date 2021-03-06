from django.urls import path
import song.views as song_views
import base.views as base_views

urlpatterns = [
    path('', song_views.SongListView.as_view(), name='song_list'),
    path('publish_song/', song_views.SongCreateView.as_view(), name='publish_song'),
    path('recognition_results/', base_views.RecognitionResultsAPIView.as_view(), name="add_recognition_result"),
    path('recognition_results/list/', base_views.RecognitionResultsList.as_view(), name="recognition_result_list"),
    path('recognition_results_summarry/', base_views.RecognitionResultsSummaryAPIView.as_view(), name="recognition_result_summary_api"),
    path('recognition_results-summary/', base_views.RecognitionResultsSummary.as_view(), name="recognition_result_summary")
]
