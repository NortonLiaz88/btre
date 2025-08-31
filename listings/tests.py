from django.test import TestCase
from .models import Listing
from realtors.models import Realtor

class ListingModelTest(TestCase):
    def setUp(self):
        self.realtor = Realtor.objects.create(name='John Doe')
        self.listing = Listing.objects.create(
            realtor=self.realtor,
            title='Test House',
            address='123 Main St',
            city='Test City',
            state='TS',
            zipcode='12345',
            price=100000,
            bedrooms=3,
            bathrooms=2,
            sqft=1500,
            lot_size=0.5,
        )

    def test_listing_creation(self):
        self.assertEqual(self.listing.title, 'Test House')