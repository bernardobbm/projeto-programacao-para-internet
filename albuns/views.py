from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from albuns.models import Album, Artist
from albuns.forms import AlbumModelForm, ArtistModelForm

def home_view(request):
    return render(request, 'home.html')

class AlbunsListView(ListView):
    model = Album
    template_name = 'albuns.html'
    context_object_name = 'albuns'

    def get_queryset(self):
        albuns = super().get_queryset().order_by('genrer')
        search = self.request.GET.get('search')

        if search:
            albuns = albuns.filter(model__icontains = search)
        return albuns

class NewAlbumCreateView(CreateView):
    model = Album
    form_class = AlbumModelForm
    template_name = 'new_album.html'
    success_url = '/albuns/'

class NewArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistModelForm
    template_name = 'new_artist.html'
    success_url = '/albuns/'
    

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumModelForm
    template_name = 'album_update.html'
    success_url = '/albuns/'