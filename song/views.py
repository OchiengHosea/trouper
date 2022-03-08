from django.shortcuts import render, redirect

from django.core.files.storage import FileSystemStorage
from artist.models import Artist
from song.models import Genre, Song
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
    
    def form_valid(self, form):
        msg = 'Category registered successfully'
        messages.add_message(self.request, messages.SUCCESS, msg)
        # form.save()

        # self.object = form.instance
        return redirect(self.get_success_url())
    
    def post(self, request, *args, **kwargs):
        form = SongForm(self.request.POST, self.request.FILES)
        file = self.request.FILES['file_name']
        fs = FileSystemStorage(location='static/', base_url='static/files')
        filenme = fs.save(file.name, file)
        
        url = fs.url(filenme)
        
        if form.is_valid():
            print("valid form")
            import pdb
            pdb.set_trace()
            song = Song.objects.create(
                title=form.data.get('title'),
                artist=Artist.objects.get(user__pk=self.request.user.pk),
                file_url=url,
                file_name=file)
            song.genres.add(form.data.get('genres'))
        else:
            print("Invalid form")
            import pdb
            pdb.set_trace()
            pass
            
        return redirect(self.get_success_url())
    
    

