from django.contrib import admin
from .models import ServiceType, Price

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('shop', 'phone_model', 'service_type', 'price', 'updated_at')
    list_filter = ('shop', 'service_type', 'phone_model__brand')
    search_fields = ('shop__name', 'phone_model__name', 'service_type__name')
    autocomplete_fields = ('shop', 'phone_model', 'service_type')
