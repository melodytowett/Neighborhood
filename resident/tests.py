import email
from os import name
from django.test import TestCase

from resident.models import Business, Neighborhood, Profile,User

# Create your tests here.
class NeighborTestClass(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="melo",email="melo@gmail.com",password="pass123")
        self.neighbor = Neighborhood(name = 'Embakasi',location = 'Nairobi',admin = user,about='This has been the best neighborhood',administrator='John doe',doctor_no='0937293',police_num='0292002')
        self.neighbor.save_hood()

    def test_get_neighborhood(self):
        my_hood = Neighborhood.my_neighbor(name)
        self.assertTrue(len(my_hood)==0)

    def test_save_hood(self):
        self.neighbor.save_hood()
        my_hood =Neighborhood.objects.all()
        self.assertTrue(len(my_hood) > 0)

class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="melo",email="melo@gmail.com",password="983di")
        self.profile = Profile(user=user,bio="This is my profile",name="melo",phone="027893",profile_pic="/image")

    def test_isntance(self):
        self.assertTrue(isinstance(self.profile,Profile)) 

    def save_profile_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        
class BusinessTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="melo",email="melo@gmail.com",password="983di")
        self.business = Business(owner=user,business_name="babyshop",business_image="/image",email="baby@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def save_business_method(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)
