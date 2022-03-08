import imp
from os import link
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePage(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        key_features = [
                dict(title='Artists', caption="Major and upcoming artists", link='artist:artist_list',),
                dict(title='Songs', caption="Curated top hits", link='song:song_list',),
                dict(title='Albums', caption="Straight from how 'twas made", link='song:song_list',)
            ]
        data = dict(
            key_features=key_features
        )
        context.update(data)
        return context