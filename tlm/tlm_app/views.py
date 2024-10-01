from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def myLists(request):
    return render(request, 'lists.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def quickTranslate(request):
    return render(request, 'quick_translate.html')

def settings(request):
    return render(request, 'settings.html')

def signup(request):
    return render(request, 'signup.html')