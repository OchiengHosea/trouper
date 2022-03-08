from django import forms

from song.models import Genre, Song

class SongForm(forms.Form):
    title = forms.CharField(max_length=125)
    genres = forms.MultipleChoiceField()
    file_name = forms.FileField()
    
    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        self.initial['genres'] = [genre.title for genre in Genre.objects.all()]
        self.fields['genres'].choices = ((genre.id, genre.title) for genre in Genre.objects.all())
    
    class Meta:
        # model = Song
        # fields = '__all__'
        # exclude = ('is_active', 'artist',)
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control border-input'}),
            'filen_name': forms.TextInput(attrs={'class':'form-control border-input'}),
            'genres': forms.SelectMultiple(
                attrs={'class': 'form-control border-input'},
                choices=(('', '')))
        }
