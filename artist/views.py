from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from artist.forms import ArtistForm
from django.urls import reverse
from artist.models import Artist
from django.shortcuts import redirect
from django.contrib import messages


class ArtistList(LoginRequiredMixin, ListView):
    model = Artist
    
    def get_queryset(self):
        return super().get_queryset()
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(artists=self.get_queryset()))
        return context
    
class ArtistSignup(LoginRequiredMixin, CreateView):
    model = Artist
    form_class = ArtistForm
    
    def get_success_url(self):
        return reverse('artist:artist_list')
    
    
    def form_valid(self, form):
        msg = 'Registered successfully'
        artist = form.save(commit=False)
        artist.user = self.request.user
        artist.save()
        messages.add_message(self.request, messages.SUCCESS, msg)
        self.object = form.instance
        return redirect(self.get_success_url())
    