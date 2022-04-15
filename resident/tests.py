import email
from os import name
from django.test import TestCase

from resident.models import Neighborhood,User

# Create your tests here.
class NeighborTestClass(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="melo",email="melo@gmail.com",password="pass123")
        self.neighbor = Neighborhood(name = 'Embakasi',location = 'Nairobi',admin = user,about='This has been the best neighborhood',administrator='John doe')
        self.neighbor.save()

    def test_get_neighborhood(self):
        my_hood = Neighborhood.my_neighbor(name)
        self.assertTrue(len(my_hood)>0)