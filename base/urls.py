from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='home'),
    path('arccloud/broadcast_results/', views.MusicResultAPIView.as_view(), name="broadcast_results")
]