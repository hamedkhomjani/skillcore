from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Shop(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100, db_index=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    verified = models.BooleanField(default=False)
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='shop')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Repair Shop"
        verbose_name_plural = "Repair Shops"

    def __str__(self):
        return f"{self.name} ({self.city})"
        
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return sum([r.rating for r in reviews]) / len(reviews)
        return 0

class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('shop', 'user') # One review per shop per user

    def __str__(self):
        return f"{self.rating} stars for {self.shop.name} by {self.user.username}"
