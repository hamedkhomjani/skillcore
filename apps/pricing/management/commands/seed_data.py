from django.core.management.base import BaseCommand
from apps.shops.models import Shop
from apps.phones.models import PhoneBrand, PhoneModel
from apps.pricing.models import ServiceType, Price
import random

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        # Phone Brands
        apple, _ = PhoneBrand.objects.get_or_create(name='Apple')
        samsung, _ = PhoneBrand.objects.get_or_create(name='Samsung')

        # Phone Models (5 models)
        iphone13, _ = PhoneModel.objects.get_or_create(brand=apple, name='iPhone 13')
        iphone14, _ = PhoneModel.objects.get_or_create(brand=apple, name='iPhone 14')
        iphone15, _ = PhoneModel.objects.get_or_create(brand=apple, name='iPhone 15')
        s23, _ = PhoneModel.objects.get_or_create(brand=samsung, name='Galaxy S23')
        s24, _ = PhoneModel.objects.get_or_create(brand=samsung, name='Galaxy S24')
        
        models = [iphone13, iphone14, iphone15, s23, s24]

        # Service Types (3 types)
        screen, _ = ServiceType.objects.get_or_create(name='Screen Replacement')
        battery, _ = ServiceType.objects.get_or_create(name='Battery Replacement')
        diagnostic, _ = ServiceType.objects.get_or_create(name='Diagnostics')
        
        services = [screen, battery, diagnostic]

        # Shops (5 shops)
        shops_data = [
            {'name': 'MobilMaster Stockholm', 'city': 'Stockholm', 'address': 'Sveavägen 45', 'verified': True},
            {'name': 'iFon Service', 'city': 'Stockholm', 'address': 'Odengatan 32', 'verified': False},
            {'name': 'Repair Express', 'city': 'Gothenburg', 'address': 'Avenyn 12', 'verified': True},
            {'name': 'FixMyPhone', 'city': 'Stockholm', 'address': 'Götgatan 10', 'verified': True},
            {'name': 'Snabbt & Billigt', 'city': 'Malmö', 'address': 'Storgatan 5', 'verified': False},
        ]

        shops = []
        for s in shops_data:
            shop, created = Shop.objects.get_or_create(name=s['name'], defaults=s)
            shops.append(shop)
            if created:
                self.stdout.write(f'Created shop: {s["name"]}')

        # Sample Prices
        # Each shop offers a price for each model/service somewhat randomly
        Price.objects.all().delete() # Clean existing prices to avoid duplicates on re-run

        count = 0
        for shop in shops:
            for model in models:
                for service in services:
                    # Random price between 500 and 3000 SEK
                    base_price = 1000 if service == screen else 500
                    if service == diagnostic:
                        base_price = 200
                    
                    price_val = base_price + random.randint(0, 10) * 50 # random increments
                    
                    Price.objects.create(
                        shop=shop,
                        phone_model=model,
                        service_type=service,
                        price=price_val
                    )
                    count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded database with {count} price entries.'))
