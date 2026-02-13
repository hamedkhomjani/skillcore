from django.db import models

class PhoneBrand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Phone Brand"
        verbose_name_plural = "Phone Brands"

    def __str__(self):
        return self.name

class PhoneModel(models.Model):
    brand = models.ForeignKey(PhoneBrand, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['brand', 'name']
        unique_together = ('brand', 'name')
        verbose_name = "Phone Model"
        verbose_name_plural = "Phone Models"

    def __str__(self):
        return f"{self.brand.name} {self.name}"
