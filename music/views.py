from django.views import generic
from django.views.generic import View
from .models import Album, Song, Video
from .form import UserForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AddAlbum(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo', 'is_favorite']


class AddSong(CreateView):
    model = Song
    fields = ['album', 'song_title', 'audio', 'is_favorite']


class AddVideo(CreateView):
    model = Video
    fields = ['album', 'video_title', 'video', 'is_favorite']


class UpdateAlbum(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo', 'is_favorite']


class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class SongView(generic.ListView):
    template_name = 'music/song.html'
    context_object_name = 'all_song'

    def get_queryset(self):
        return Song.objects.all()


class VideoView(generic.ListView):
    template_name = 'music/video.html'
    context_object_name = 'all_video'

    def get_queryset(self):
        return Video.objects.all()


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/register.html'

    #fill form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #submit
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #Cleaned Data(Standard format)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            #return user object if credentials are correct
            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request,self.template_name,{'form':form})




























