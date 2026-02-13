from django.contrib import admin
from .models import Shop, Review

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'verified', 'created_at')
    list_filter = ('verified', 'city')
    search_fields = ('name', 'city', 'address')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('shop', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'shop')
    search_fields = ('shop__name', 'user__username', 'comment')
