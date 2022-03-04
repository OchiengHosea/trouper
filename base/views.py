import imp
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePage(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        key_features = [
                dict(title='Artists', caption="Major and upcoming artists"),
                dict(title='Playlists', caption="Curated top hits"),
                dict(title='Albums', caption="Straight from how 'twas made")
            ]
        data = dict(
            key_features=key_features
        )
        context.update(data)
        return context