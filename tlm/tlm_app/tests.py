from django.test import TestCase
from django.contrib.auth.models import User
from tlm_app.models import *

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
        self.assertIsNotNone(superuserList.filter(username='michael'))
        self.assertIsNotNone(superuserList.filter(username='cole'))
        self.assertIsNotNone(superuserList.filter(username='brett'))
        self.assertIsNotNone(superuserList.filter(username='aman')) '''

# Test cases for storing translation history
class UserTranslationHistoryTests(TestCase):
    # Test ability to add to a specific user's translation history
    def test_addTranslationHistory(self):
        newUser = User.objects.create(username='Jane_Doe', email='jD0e@gmail.com', password='b45e32S') # Create new user to assign an entry for translation history
        newEntry = UserTranslationHistory.objects.create(user=newUser, originalLanguage='Spanish', translatedIntoLanguage='English', originalText='Konnichiwa', translatedText='Hello')

        dummyUser = User.objects.create(username='xXx_johnSmith_xXx', email='john.2000@gmail.com', password='12345') # Create new user to test if correct user is being assigned translation history

        self.assertIsNotNone(newEntry) # Test that translation history entry is created

        # Test that translation history is correctly assigned to correct user
        self.assertTrue(newEntry.user==newUser) 
        self.assertFalse(newEntry.user==dummyUser)
