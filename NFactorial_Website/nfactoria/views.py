from django.contrib.auth import authenticate
from django.shortcuts import render
from nfactoria.models import Music
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Music, Review
from .forms import ReviewForm
def index(request):
    music = Music.objects.all()
    return render(request, 'index.html', {'music': music})
def musics(request):
    music = Music.objects.all()
    return render(request, 'nfactoria/musics.html', {'music': music})
def search(request):
    query = request.GET.get('query')
    music = Music.objects.all()
    qs = music.filter(name__icontains=query)

    return render(request, 'nfactoria/search.html', {'music': qs})
def search_by_genre(request):
    query = request.GET.get('query')
    music = Music.objects.all()
    qs = music.filter(genre__icontains=query)

    return render(request, 'nfactoria/search_by_genre.html', {'music': qs})
def musicpost(request,id):
    music = Music.objects.filter(music_id=id).first()
    reviews = music.reviews.all()
    stars = range(1, 6)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.music = music
            review.user = request.user
            review.save()
            return redirect('/')
    else:
        form = ReviewForm()

    return render(request, 'nfactoria/musicpost.html',
                  {'music': music, 'reviews': reviews, 'form': form, 'stars': stars})

def login(request):
    if request.method == "POST":
        nickname = request.POST['nickname']
        password = request.POST['password']
        user = authenticate(nickname=nickname,password=password)
        from django.contrib.auth import login
        login(request, user)
        return redirect('index')
    return render(request, 'nfactoria/login.html')

def signup(request):

    if request.method == "POST":
        name = request.POST['name']
        nickname = request.POST['nickname']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(nickname, email, password)
        myuser.name = name
        myuser.save()
        from django.contrib.auth import login
        login(request,myuser)
        return redirect('index')
    return render(request, 'nfactoria/signup.html')

