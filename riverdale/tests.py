from calendar import c
import email
from turtle import up, update
from django.test import TestCase
from .models import Business, Neighborhood,User

# Create your tests here.
class NeigbourhoodTestCase(TestCase):

    def setUp(self):
        self.phase4 = Neighborhood(title="Karen",id=3,location="yala-Road",occupants_count="200")

    def test_instance(self):
        self.assertTrue(isinstance(self.phase4,Neighborhood))

    def test_get_neighborhood_id(self,id):
      self.phase4.neighborhood_id()
      n=Neighborhood.objects.get(id=1)
      self.assertTrue(len(n)>0)

    # update
    def test_update_neighborhood(self,current_neighborhood,new_neighborhood):
        self.phase4.update_neighborhood(current_neighborhood,new_neighborhood)
        update_neighborhood=Neighborhood.objects.all()
        self.assertTrue(len(update_neighborhood)>0)

    # Testing Save Method
    def test_save_method(self):
        self.phase4.save_neighborhood()
        neighborhoods= Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) > 0)

    # create 
    def test_create_neighborhood(self):
        self.assertIsInstance(self.phase4, Neighborhood)

    # delete
    def test_tear_down(self):
        Neighborhood.objects.all().delete()
    
    


# # business
class BusinessTestCase(TestCase):

    def setUp(self):
        self.butcher = Business(b_name="leshanButcher",contacts="0712347809",email="butche@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.butcher,Business))

    def test_get_business_id(self,id):
      self.phase4.business_id()
      n=Business.objects.get(id=1)
      self.assertTrue(len(n)>0)

    # update
    def test_update_business(self):
        self.phase4.update_business()
        update_business=Business.objects.all()
        self.assertTrue(len(update_business)>0)

#     # Testing Save Method
    def test_save_method(self):
        self.butcher.save_business()
        businessess= Business.objects.all()
        self.assertTrue(len(businessess) > 0)

#     # create 
    def test_create_business(self):
        self.assertIsInstance(self.butcher, Business)

    # delete
    def test_tear_down(self):
        Business.objects.all().delete()
    
    



