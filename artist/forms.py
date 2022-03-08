from artist.models import Artist
from django import forms

class ArtistForm(forms.ModelForm):
    
    class Meta:
        model = Artist
        fields = '__all__'
        exclude = ('is_active','user',)
