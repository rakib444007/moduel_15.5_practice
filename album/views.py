from django.shortcuts import render,redirect
from album.models import Album
from album.forms import AlbumForm

# Create your views here.


def album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('album')
    else:
        form = AlbumForm()
    return render(request,'add_album.html',{'form': form})



def album_edit(request,id):
    data = Album.objects.get(pk=id)
    form= AlbumForm(instance=data)
    if request.method == 'POST':
        form = AlbumForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'add_album.html',{'form' : form})
