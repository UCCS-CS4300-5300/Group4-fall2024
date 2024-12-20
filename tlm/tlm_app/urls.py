from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.contrib.auth import views as auth_views


def custom_logout_view(request):
    messages.success(request, "You've been logged out. See you later!")
    return LogoutView.as_view(next_page='index')(request)


urlpatterns = [
    path('', views.index, name='index'),  # Index page url
    path('about/', views.about, name='about'),  # About page url
    path('lists/', views.myLists, name='lists'),  # My list page url
    path('list_entries/', views.listEntries, name='listEntries'),
    path('profile/', views.profile, name='profile'),  # Profile page url
    # Quick translate page url
    path('quick_Translate', views.quickTranslate, name='quick_Translate'),
    path('settings', views.settings, name='settings'),  # Settings page url
    path('register', views.register, name='register'),  # Register page url
    path('logout/', custom_logout_view, name='logout'),  # Logout page url
    # Login page url
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='appLogin'
    ),
    path('api/speak/', views.speak, name='speak'),
    path('toggleDarkMode', views.toggleDarkMode, name='toggleDarkMode'),
    path('lists/addToList', views.addToUserList, name='addToList'),
    # Update account URL
    path('profile/update/', views.update_account, name='update_account'),
    path('api/get-definition/', views.get_definition, name='get_definition'),
    path('addEntry', views.addUserListEntry, name="addEntry"),
    path('list_entries/deleteEntry', views.deleteUserListEntry, name="deleteEntry"),
    path('list_entries/addFromEntry', views.addFromEntry, name="addFromEntry")
]
