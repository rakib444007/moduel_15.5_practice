from django.shortcuts import render,redirect
from .models import Musician
from .forms import MusicianForm
# Create your views here.


def musician(request):
    if request.method == 'POST':
        data = MusicianForm(request.POST)
        if data.is_valid():
            data.save()
            print(data.cleaned_data)
            return redirect('musician')
    else:
        data = MusicianForm()
    return render(request,'add_musician.html',{'data' : data})
        
def musician_delete(request,id):
    form = Musician.objects.get(pk=id)
    form.delete()
    return redirect('homepage')

def musician_edit (request,id):
    data = Musician.objects.get(pk=id)
    form= MusicianForm(instance=data)
    if request.method == 'POST':
        form = MusicianForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'add_musician.html',{'data' : form})

