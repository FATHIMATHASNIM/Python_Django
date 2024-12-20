from django.core.management.base import BaseCommand
from store.models import Product  # Assuming Product model is in store app
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate the database with fake products'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Set the number of fake products to generate
        num_products = 100

        for _ in range(num_products):
            product = Product(
                title=fake.word().capitalize(),
                description=fake.text(),
                price=random.randint(10, 100),  # Random price between 10 and 100
                image_url=fake.image_url()  # Faker can generate random image URLs
            )
            product.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created {num_products} fake products'))
