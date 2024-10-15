from django.shortcuts import render, redirect
from .forms import QuickTranslateForm
import translators as ts
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def myLists(request):
    return render(request, 'lists.html')

def profile(request):
    return render(request, 'profile.html')

def quickTranslate(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['t_text'] = ts.translate_text(data['q_text'], from_language=data['q_lang'], to_language=data['t_lang'])
        form = QuickTranslateForm(data)
    else:
        form = QuickTranslateForm()
    context = {'form': form}
    return render(request, 'quick_translate.html', context)

def settings(request):
    return render(request, 'settings.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('index')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')