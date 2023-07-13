from django import forms
from albuns.models import Album, Artist
import datetime

class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def clean_release_year(self):
        release_year = self.cleaned_data.get('release_year')
        today = datetime.date.today()
        year = today.year

        if release_year > year:
            self.add_error('release_year','Ano de lançamento não pode ser maior que o ano atual')

class ArtistModelForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'