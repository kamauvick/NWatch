from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import *


@login_required(login_url='login')
def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    try:
        hoods = Neighbourhood.objects.all()
        profiles = Profile.objects.all()
        biz = Business.objects.all()
        emergencies = EmergencyContact.objects.all()
        posts = Post.objects.all()

        index_data = {
            'hoods': hoods,
            'profiles': profiles,
            'businesses': biz,
            'emergencies': emergencies,
            'posts': posts,
            'form': form,
        }

    except Neighbourhood.DoesNotExist:
        posts = None
        hoods = None
        profiles = None
        biz = None
        emergencies = None
    return render(request, 'main/index.html', index_data)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = request.user.profile.estate
            post.owner = request.user
            post.save()
    else:
        form = PostForm()
    return render(request, 'model_temp/add_posts.html', {'form': form})


@login_required(login_url='login')
def create_hood(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()
    else:
        form = NeighbourhoodForm
    return render(request, 'model_temp/add_hoods.html', {'form': form})


@login_required(login_url='login')
def create_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.save()
    else:
        form = BusinessForm
    return render(request, 'model_temp/add_biz.html', {'form': form})


@login_required(login_url='login')
def create_emergency(request):
    if request.method == 'POST':
        form = EmergencyForm(request.POST, request.FILES)
        if form.is_valid():
            emergency = form.save(commit=False)
            emergency.save()
    else:
        form = EmergencyForm
    return render(request, 'model_temp/add_emergency.html', {'form': form})


def about(request):
    name = 'vick'
    return render(request, 'main/about.html', {'name': name})


def profile(request, username):
    return render(request, 'main/profile.html')


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'editing/edit_profile.html', {'form': form})


def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        print(search_term)
        searched_photos = Neighbourhood.search_by_title(search_term)
        print(searched_photos)
        message = f'{search_term}'
        params = {
            'searched_photos': searched_photos,
            'message': message,
        }

        return render(request, 'search_results.html', params)

    else:
        message = 'Ooppss, You did not search for anything.'
        return render(request, 'main/search_results.html', locals())
