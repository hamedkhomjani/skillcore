from django.db import models
from apps.shops.models import Shop
from apps.phones.models import PhoneModel

class ServiceType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Service Type"
        verbose_name_plural = "Service Types"

    def __str__(self):
        return self.name

class Price(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='prices')
    phone_model = models.ForeignKey(PhoneModel, on_delete=models.CASCADE, related_name='prices')
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Proper indexing for search optimization
        indexes = [
            models.Index(fields=['phone_model', 'service_type', 'price']),
            models.Index(fields=['shop', 'phone_model']),
        ]
        unique_together = ('shop', 'phone_model', 'service_type')
        ordering = ['price']
        verbose_name = "Price"
        verbose_name_plural = "Prices"

    def __str__(self):
        return f"{self.shop.name} - {self.phone_model} - {self.service_type}: {self.price}"
