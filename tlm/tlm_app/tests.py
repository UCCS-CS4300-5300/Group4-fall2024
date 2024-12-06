from django.test import TestCase, Client
from django.contrib.auth.models import User
from tlm_app.models import *
from django.urls import reverse
import json

# Create your tests here.

# Test cases for normal user accounts
class NormalUserTestCases(TestCase):
    # Test ability to add regular users
    def test_addNewUser(self):
        newUser = User.objects.create(username='xXx_johnSmith_xXx', email='john.2000@gmail.com', password='12345') # Create new regular user

        self.assertIsNotNone(User.objects.filter(username='xXx_johnSmith_xXx')) # Test that user is created
        self.assertFalse(newUser.is_superuser) # Tests that user is normal user

# Test cases for superuser accounts
class SuperUserTestCases(TestCase):
    # Test ability to add superusers
    def test_addSuperUser(self):
        newAdmin = User.objects.create_superuser('suppa', 'test@email.com', 'password') #Create new superuser

        self.assertIsNotNone(newAdmin) # Test new superuser was created
        self.assertTrue(newAdmin.is_superuser)# Test that new user is superuser

    # Test that the dev team are superusers
    ''' def test_devTeamAreSuperUsers(self):
        superuserList = User.objects.filter(is_superuser=True)
        self.assertIsNotNone(superuserList.filter(username='cameron'))
        self.assertIsNotNone(superuserList.filter(username='michael'))pip 
        self.assertIsNotNone(superuserList.filter(username='cole'))
        self.assertIsNotNone(superuserList.filter(username='brett'))
        self.assertIsNotNone(superuserList.filter(username='aman')) '''

# Test cases for storing translation history
class UserTranslationHistoryTests(TestCase):

     # Set up a test user
    def setUp(self):
        self.user = User.objects.create(username='Test_User', email='TestUser@gmail.com', password='TestingTesting123')  

    # Test translation history entry
    def test_addTranslationHistory(self):
        newEntry = UserTranslationHistory.objects.create(
            user=self.user,
            sourceLanguage='Spanish',
            sourceText='Hola',
            targetLanguage='English',
            targetText='Hello',
        )
        self.assertIsNotNone(newEntry)  
        self.assertEqual(newEntry.user, self.user)  
   
    # Test the limit of translation history entries
    def test_translation_history_limit(self):
        for i in range(12):
            UserTranslationHistory.objects.create(
                user=self.user,
                sourceLanguage='English',
                sourceText=f'Word {i}',
                targetLanguage='Spanish',
                targetText=f'Palabra {i}',
            )
        self.assertEqual(UserTranslationHistory.objects.filter(user=self.user).count(), 10)  

    # Test the order of translation history entries
    def test_translation_history_order(self):
        entry1 = UserTranslationHistory.objects.create(user=self.user, sourceText='First', targetText='Primero')
        entry2 = UserTranslationHistory.objects.create(user=self.user, sourceText='Second', targetText='Segundo')
        latest_entry = UserTranslationHistory.objects.order_by('-dateCreated').first()
        self.assertEqual(latest_entry, entry2)  


# Test cases for user settings
class UserSettingsTests(TestCase):

    # Set up a test user
    def setUp(self):
        self.user = User.objects.create(username='Test_User', password='TestingTesting123')

    # Test the creation of user settings
    def test_create_user_settings(self):
        settings = UserSettings.objects.create(user=self.user, darkModeToggle=True, defaultLanguage='English')
        self.assertIsNotNone(settings)
        self.assertTrue(settings.darkModeToggle)

    # Test toggling dark mode settings
    def test_toggle_dark_mode(self):
        settings = UserSettings.objects.create(user=self.user, darkModeToggle=False)
        settings.darkModeToggle = True
        settings.save()
        self.assertTrue(UserSettings.objects.get(user=self.user).darkModeToggle)


# Test cases for list entries
class UserListEntryTests(TestCase):

    # Set up a test user
    def setUp(self):
        self.user = User.objects.create(username='Test_User', password='TestingTesting123')
        self.user_list = UserListObject.objects.create(user=self.user, listTitle='My List')

    # Test adding a new entry to the user list
    def test_add_list_entry(self):
        entry = UserListEntry.objects.create(
            userList=self.user_list,
            sourceLanguage='English',
            sourceText='Cat',
            targetLanguage='Spanish',
            targetText='Gato',
        )
        self.assertIsNotNone(entry)
        self.assertEqual(entry.userList, self.user_list)

    # Test the list entry definition
    def test_list_entry_string_representation(self):
        entry = UserListEntry.objects.create(
            userList=self.user_list,
            sourceLanguage='English',
            sourceText='Dog',
            targetLanguage='Spanish',
            targetText='Perro',
        )
        self.assertEqual(str(entry), 'Dog - Perro')


# Test cases for views
class ViewTestsCases(TestCase):

    # Set up a test user and login
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='Test_User', password='TestingTesting123')
        self.client.login(username='Test_User', password='TestingTesting123')
        self.user_list = UserListObject.objects.create(user=self.user, listTitle='Test List')
        UserSettings.objects.create(user=self.user, darkModeToggle=False)  

    # Test get request to for Quick Translate
    def test_quick_translate_get(self):
        response = self.client.get(reverse('quick_Translate'))
        self.assertEqual(response.status_code, 200)

    # Test valid POST request to QuickTranslateView
    def test_quick_translate_post_valid_data(self):
        data = {
            'sourceLanguage': 'en',
            'targetLanguage': 'es',
            'sourceText': 'Hello',
        }
        response = self.client.post(reverse('quick_Translate'), data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    # Test invalid POST request to QuickTranslateView
    def test_quick_translate_post_invalid_data(self):
        data = {
            'sourceLanguage': '',
            'targetLanguage': '',
            'sourceText': '',
        }
        response = self.client.post(reverse('quick_Translate'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'sourceLanguage', 'This field is required.')

    # Test authenticated access to the "My Lists" view
    def test_my_lists_view_authenticated(self):
        response = self.client.get(reverse('lists'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lists.html')
        self.assertIn('userLists', response.context)

    # Test unauthenticated access to the "My Lists" view
    def test_my_lists_view_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse('lists'))
        self.assertEqual(response.status_code, 302)  

    # Test GET request to the "List Entries" view
    def test_list_entries_view_get(self):
        response = self.client.get(reverse('listEntries'), {'listId': self.user_list.pk})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_content.html')
        self.assertIn('entries', response.context)

    # Test POST request to the "List Entries" view
    def test_list_entries_view_post(self):
        response = self.client.post(reverse('listEntries'), {'selectedList': self.user_list.pk})
        self.assertRedirects(response, f"{reverse('listEntries')}?listId={self.user_list.pk}")

    # Test enabling dark mode via POST request to the "Toggle Dark Mode" view
    def test_toggle_dark_mode_post_enabled(self):
        data = {'darkModeStatus': 'True'}
        response = self.client.post(reverse('toggleDarkMode'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': 1})

    # Test disabling dark mode via POST request to the "Toggle Dark Mode" view
    def test_toggle_dark_mode_post_disabled(self):
        data = {'darkModeStatus': 'False'}
        response = self.client.post(reverse('toggleDarkMode'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': 1})

    # Test GET request to retrieve dark mode status for an authenticated user
    def test_toggle_dark_mode_get_authenticated(self):
        response = self.client.get(reverse('toggleDarkMode'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': 1, 'darkModeStatus': 'False'})

    # Test GET request to retrieve dark mode status for an unauthenticated user
    def test_toggle_dark_mode_get_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse('toggleDarkMode'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': 0, 'error': 'User not authenticated'})

    # Test creating a new user list via POST request
    def test_add_to_user_list_post(self):
        data = {'userListTitle': 'New List'}
        response = self.client.post(reverse('addToList'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': 1, 'list': 'New List Created'})
        self.assertTrue(UserListObject.objects.filter(user=self.user, listTitle='New List').exists())

    # Test deleting a user list via DELETE request
    def test_add_to_user_list_delete(self):
        data = {'listTitle': self.user_list.listTitle}
        response = self.client.delete(reverse('addToList'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': 1, 'list': 'List Deleted'})
        self.assertFalse(UserListObject.objects.filter(user=self.user, listTitle=self.user_list.listTitle).exists())

    # Test invalid data submission during user registration
    def test_register_view_post_invalid(self):
        data = {'username': '', 'password1': 'password', 'password2': 'password'}
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertContains(response, 'This field is required.')

    # Test "Speak" API for generating audio
    def test_speak_view(self):
        response = self.client.get(reverse('speak'), {'text': 'Hello', 'lang': 'en'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'audio/mpeg')

    # Test fetching definition for a valid word
    def test_get_definition_valid_word(self):
        response = self.client.get(reverse('get_definition'), {'word': 'hello', 'lang': 'en'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('definitions', response.json())

    # Test fetching definition for a invalid word
    def test_get_definition_invalid_word(self):
        response = self.client.get(reverse('get_definition'), {'word': '', 'lang': 'en'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json())