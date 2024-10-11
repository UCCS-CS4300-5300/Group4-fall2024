from django.shortcuts import render
from .forms import QuickTranslateForm
import translators as ts

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

def signup(request):
    return render(request, 'signup.html')