import random

from django.core.management.base import BaseCommand
from faker import Faker

from listings.models import Listing
from realtors.models import Realtor


class Command(BaseCommand):
    help = "Seeds the database with listings"

    def handle(self, *args, **options):
        self.stdout.write("Seeding listings...")
        fake = Faker()
        realtors = Realtor.objects.all()
        for _ in range(10):
            Listing.objects.create(
                realtor=random.choice(realtors),
                title=fake.sentence(nb_words=5),
                address=fake.address(),
                city=fake.city(),
                state=fake.state(),
                zipcode=fake.zipcode(),
                description=fake.text(),
                price=fake.random_int(min=100000, max=1000000),
                bedrooms=fake.random_int(min=1, max=5),
                bathrooms=fake.random_int(min=1, max=3),
                garage=fake.random_int(min=0, max=2),
                sqft=fake.random_int(min=500, max=5000),
                lot_size=round(random.uniform(0.1, 1.0), 1),
                is_published=True,
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded listings"))
