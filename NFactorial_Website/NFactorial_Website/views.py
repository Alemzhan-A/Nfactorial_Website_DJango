from django.shortcuts import render
from nfactoria.models import Music
def index(request):
    music = Music.objects.all()
    return render(request, 'index.html', {'music': music})

def musics(request):
    return render(request, 'nfactoria/musics.html')
