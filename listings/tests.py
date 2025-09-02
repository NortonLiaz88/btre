"""Module docstring."""

from django.test import TestCase

from realtors.models import Realtor

from .models import Listing


class ListingModelTest(TestCase):
    """Listing model test."""
    def setUp(self):
        """Set up test."""
        self.realtor = Realtor.objects.create(name="John Doe")
        self.listing = Listing.objects.create(
            realtor=self.realtor,
            title="Test House",
            address="123 Main St",
            city="Test City",
            state="TS",
            zipcode="12345",
            price=100000,
            bedrooms=3,
            bathrooms=2,
            sqft=1500,
            lot_size=0.5,
        )

    def test_listing_creation(self):
        """Test listing creation."""
        self.assertEqual(self.listing.title, "Test House")
