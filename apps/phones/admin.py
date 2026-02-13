from django.contrib import admin
from .models import PhoneBrand, PhoneModel

@admin.register(PhoneBrand)
class PhoneBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(PhoneModel)
class PhoneModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand')
    list_filter = ('brand',)
    search_fields = ('name', 'brand__name')
