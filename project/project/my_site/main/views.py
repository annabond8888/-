from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main.forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'main/login1.html', {'form': form, 'error': 'Неверное имя пользователя или пароль.'})
    else:
        form = LoginForm()
    return render(request, 'main/login1.html', {'form': form})

def index(request):
    return render(request, "main/index.html")

def home(request):
    return render(request, "main/home.html")

def help(request):
    return render(request, "main/help.html")

def about(request):
    return render(request, "main/about.html")

def map(request):
    return render(request, "main/map.html")

def show_login_page(request):
    return render(request, "main/login.html")

def games(request):
    return render(request, "main/games.html")

def signup(request):
    return render(request, "main/signup.html")

def login1(request):
    return render(request, "main/login1.html")