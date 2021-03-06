from django.shortcuts import render, redirect

from django.core.files.storage import FileSystemStorage
from artist.models import Artist
from song.models import Genre, Recorder, Song
from django.views.generic import CreateView, ListView
from song.forms import SongForm
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class SongListView(ListView):
    model = Song
    queryset = model.objects.all()
    
    def get_queryset(self):
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(songs=self.get_queryset()))
        return context
class SongCreateView(LoginRequiredMixin, CreateView):
    model = Song
    form_class = SongForm
    
    def get_form(self):
        return self.form_class()
    
    def get_success_url(self):
        return reverse('song:song_list')
    
    # def form_valid(self, form):
    #     msg = 'Category registered successfully'
    #     messages.add_message(self.request, messages.SUCCESS, msg)
    #     form.save()

    #     self.object = form.instance
    #     return redirect(self.get_success_url())
    
    def post(self, request, *args, **kwargs):
        form = SongForm(self.request.POST, self.request.FILES)
        file = self.request.FILES['file_name']
        fs = FileSystemStorage(location=f'media/uploads/{request.user.username}/', base_url=f'/media/uploads/{request.user.username}/')
        filenme = fs.save(file.name, file)
        
        url = fs.url(filenme)
        
        if form.is_valid():
            song = Song.objects.create(
                title=form.data.get('title'),
                artist=Artist.objects.filter(user__pk=self.request.user.pk).first(),
                file_url=url,
                file_name=file.name)
            song.genres.add(form.data.get('genres'))
        else:
            print("Invalid form")
            
            pass
            
        return redirect(self.get_success_url())
    
class RecorderListView(ListView):
    model = Recorder
    
    def get_queryset(self):
        return super().get_queryset()
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recorders"] = self.get_queryset
        return context
    
