from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Index page url
    path('about/', views.about, name='about'), # About page url
    path('lists/', views.myLists, name='lists'), # My list page url
    path('login/', views.login, name='login'), # Login page url
    path('profile/', views.profile, name='profile'), # Profile page url
    path('quick_Translate', views.quickTranslate, name='quick_Translate'), # Quick translate page url
    path('settings', views.settings, name='settings'), # Settings page url 
    path('signup', views.signup, name='signup') # Sign up page url
]