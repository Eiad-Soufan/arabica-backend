from django.db import models
from .constants import STATUS_CHOICES


class Category(models.Model):
    name_ar = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    name_ms = models.CharField(max_length=150)

    image_url = models.URLField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="published"
    )

    def __str__(self):
        return self.name_en


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE
    )

    name_ar = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    name_ms = models.CharField(max_length=150)

    description_ar = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_ms = models.TextField(blank=True)

    price = models.DecimalField(max_digits=8, decimal_places=2)
    promo_price = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    is_recommended = models.BooleanField(default=False, db_index=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="published"
    )

    def __str__(self):
        return self.name_en


class HeroImage(models.Model):
    image_url = models.URLField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="published"
    )

    def __str__(self):
        return f"Hero Image #{self.id}"

class SmallBanner(models.Model):
    image_url = models.URLField()   
    link = models.CharField(max_length=500, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="published"
    )

    def __str__(self):
        return f"SmallBanner #{self.id}"




class Promotion(models.Model):
    image_url = models.URLField()
    link = models.CharField(max_length=500, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="published"
    )

    def __str__(self):
        return f"Promotion #{self.id}"


class GalleryImage(models.Model):
    image_url = models.URLField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="published"
    )

    def __str__(self):
        return f"Gallery Image #{self.id}"
    
class Video(models.Model):
    video_url = models.URLField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="published"
    )

    def __str__(self):

        return f"Video #{self.id}"




class PromotionCategory(models.Model):
    name_ar = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    name_ms = models.CharField(max_length=150)

    image_url = models.URLField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="published"
    )

    def __str__(self):
        return self.name_en


class PromotionProduct(models.Model):
    category = models.ForeignKey(
        PromotionCategory,
        related_name="products",
        on_delete=models.CASCADE
    )

    name_ar = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    name_ms = models.CharField(max_length=150)

    description_ar = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_ms = models.TextField(blank=True)

    price = models.DecimalField(max_digits=8, decimal_places=2)
    promo_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    is_recommended = models.BooleanField(default=False, db_index=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="published"
    )

    def __str__(self):
        return self.name_en

