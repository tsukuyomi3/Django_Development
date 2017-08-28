from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'register/$', views.UserFormView.as_view(), name='register'),

    #music/song/
    url(r'songs/$', views.SongView.as_view(), name='song'),

    #music/video/
    url(r'videos/$', views.VideoView.as_view(), name='video'),

    # music/71/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #music/album/add
    url(r'album/add/$', views.AddAlbum.as_view(), name='add-album'),

    #music/song/add
    url(r'song/add/$', views.AddSong.as_view(), name='add-song'),

    #music/video/add
    url(r'video/add/$', views.AddVideo.as_view(), name='add-video'),

    #music/album/edit/2/
    url(r'album/edit/(?P<pk>[0-9]+)/$', views.UpdateAlbum.as_view(), name='update-album'),

    #music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.DeleteAlbum.as_view(), name='delete-album'),

]
