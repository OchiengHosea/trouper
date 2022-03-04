from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from artist.models import Artist


class ArtistList(LoginRequiredMixin, TemplateView):
    template_name = 'artist/artist_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[""] = {}
        return context
    
class ArtistSignup(CreateView):
    model = Artist