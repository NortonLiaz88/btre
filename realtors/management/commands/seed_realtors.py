from django.core.management.base import BaseCommand
from faker import Faker

from realtors.models import Realtor


class Command(BaseCommand):
    help = "Seeds the database with realtors"

    def handle(self, *args, **options):
        self.stdout.write("Seeding realtors...")
        fake = Faker()
        for _ in range(10):
            Realtor.objects.create(
                name=fake.name(),
                description=fake.text(),
                email=fake.email(),
                phone=fake.numerify(text="###-###-####"),
                is_mvp=fake.boolean(),
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded realtors"))
