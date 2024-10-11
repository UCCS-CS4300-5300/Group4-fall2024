from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class SuperUserTestCases(TestCase):
    # Test the ability to add superusers
    def test_addSuperUser(self):
        newAdmin = User.objects.create_superuser('newUser', 'test@email.com', 'password') #Create new superuser

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


