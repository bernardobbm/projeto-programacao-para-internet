from types import NoneType
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

        if isinstance(release_year, NoneType):
            return self.add_error('release_year','Ano de lançamento deve conter um número de ano')

        if release_year > year:
            self.add_error('release_year','Ano de lançamento não pode ser maior que o ano atual')
        
        if release_year < 1800:
            return self.add_error('release_year','Ano de lançamento não pode ser de um ano inferior a 1800')
        
        return release_year

    def clean_number_of_sales(self):
        number_of_sales = self.cleaned_data.get('number_of_sales')

        if isinstance(number_of_sales, NoneType):
            return self.add_error('number_of_sales','Número de vendas deve conter um número')

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')

        if not photo:
            return self.add_error('photo','Você precisa adicionar uma foto de capa para o album')

        return photo

class ArtistModelForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'