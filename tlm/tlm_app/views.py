from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuickTranslateForm, UserRegisterForm
from .models import *
import translators as ts
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from gtts import gTTS
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.db.models import *
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def myLists(request):
    userLists = UserListObject.objects.filter(user=request.user)
    context = {'userLists': userLists}
    return render(request, 'lists.html', context)

@login_required
def listEntries(request):
    selectedList = get_object_or_404(UserListObject, pk=request.POST.get('selectedList'))
    listEntries = UserListEntry.objects.filter(userList = selectedList)
    context = {"entries": listEntries}
    return render(request, 'list_content.html', context)

def profile(request):
    return render(request, 'profile.html')

def quickTranslate(request):
    if request.method == 'POST':
        source_lang = request.POST.get('sourceLanguage')
        target_lang = request.POST.get('targetLanguage')
        data = request.POST.copy()

        if source_lang == target_lang:
            data['targetText'] = data['sourceText']
        else:
            data['targetText'] = ts.translate_text(data['sourceText'], from_language=source_lang, to_language=target_lang)

        form = QuickTranslateForm(data)
        if form.is_valid() and request.user.is_authenticated:
            translation = form.save(commit=False)
            translation.user = request.user
            translation.save()
    else:
        form = QuickTranslateForm()

    context = {'form': form}

    if request.user.is_authenticated:
        translationHistory = UserTranslationHistory.objects.filter(user=request.user).order_by('-dateCreated')
        context['translationHistory'] = translationHistory
        
    return render(request, 'quick_translate.html', context)

def get_definition(request):
    word = request.GET.get('word')
    lang = request.GET.get('lang', 'en')  

    if word:
        api_url = f"https://api.dictionaryapi.dev/api/v2/entries/{lang}/{word}"
        response = requests.get(api_url)

        if response.status_code == 200:
            definitions = response.json()[0].get('meanings', [])
            definition_texts = [meaning['definitions'][0]['definition'] for meaning in definitions]
            return JsonResponse({'definitions': definition_texts})
        else:
            return JsonResponse({'error': 'No definition found for the word.'})
    return JsonResponse({'error': 'Invalid request.'})


def settings(request):
    return render(request, 'settings.html')

@csrf_exempt
def toggleDarkMode(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            darkModeStatus = data.get('darkModeStatus')

            if darkModeStatus == 'True':
                darkModeStatus = True
            elif darkModeStatus == 'False':
                darkModeStatus = False
            else:
                darkModeStatus = bool(darkModeStatus) 

            user = request.user  

            if user.is_authenticated:
                darkModeSetting, created = UserSettings.objects.get_or_create(user=user)
                
                darkModeSetting.darkModeToggle = darkModeStatus
                darkModeSetting.save()


                return JsonResponse({'success': 1})
            else:
                return JsonResponse({'success': 0, 'error': 'User not found'})

        except json.JSONDecodeError:
            return JsonResponse({'success': 0, 'error': 'Invalid JSON data'})
    elif request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            try:
                darkModeSetting = UserSettings.objects.get(user=user)
                return JsonResponse({'success': 1, 'darkModeStatus': 'True' if darkModeSetting.darkModeToggle else 'False'})
            except UserSettings.DoesNotExist:
                return JsonResponse({'success': 0, 'darkModeStatus': 'False'})
        else:
            return JsonResponse({'success': 0, 'error': 'User not authenticated'})
    else:
        return JsonResponse({'success': 0, 'error': 'Invalid request method'})

@csrf_exempt
def addToUserList(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            listName = data.get('userListTitle')

            newList = UserListObject.objects.update_or_create(
                user = request.user,
                listTitle = listName
            )

            return JsonResponse({'success': 1, 'list': 'New List Created'})
        except json.JSONDecodeError:
            return JsonResponse({'success': 0, 'error': 'Invalid JSON data'})
    else:
        return JsonResponse({'success': 0, 'error': 'Invalid request method'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            newUser = form.save()

            login(request, newUser)

            # Creates a user settings profile for user
            settingsProfile = UserSettings.objects.create(
                user = newUser,
                darkModeToggle = False,
                defaultLanguage = "English"
            )

            messages.success(request, f'Your account has been created! You are now logged in!')

            return redirect('index')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def appLogin(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def speak(request):
    text = request.GET.get('text', '')
    lang = request.GET.get('lang', 'en')
    tts = gTTS(text, lang=lang)
    response = HttpResponse(content_type='audio/mpeg')
    tts.write_to_fp(response)
    return response


@login_required
def update_account(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Update user information
        user.username = username
        user.email = email
        user.save()

        # Display success message and redirect to profile page
        messages.success(request, 'Account updated successfully!')
        return redirect('profile')
    else:
        # Render profile page with existing values
        context = {
            'user': user,
        }
        return render(request, 'profile.html', context)

