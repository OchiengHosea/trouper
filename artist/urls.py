from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArtistList.as_view(), name='artist_list'),
    path('signup/', views.ArtistSignup.as_view(), name='artist_signup'),
]