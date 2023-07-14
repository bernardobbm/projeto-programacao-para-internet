from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from albuns.views import AlbunsListView, home_view, NewAlbumCreateView, AlbumDetailView, AlbumDeleteView, AlbumUpdateView, NewArtistCreateView
from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('albuns/', AlbunsListView.as_view(), name='albuns_list'),
    path('new_album/', NewAlbumCreateView.as_view(), name='new_album'),
    path('new_artist/', NewArtistCreateView.as_view(), name='new_artist'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name='album_update'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
