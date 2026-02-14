from django.contrib import admin
from .models import (
    Category,
    Product,
    HeroImage,
    SmallBanner,
    Promotion,
    GalleryImage,
    Video,
    PromotionCategory,      # ✅ NEW
    PromotionProduct,       # ✅ NEW
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name_en", "status")
    list_filter = ("status",)
    search_fields = ("name_ar", "name_en", "name_ms")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_en",
        "category",
        "price",
        "promo_price",
        "is_recommended",
        "status",
    )
    list_filter = ("status", "is_recommended", "category")
    search_fields = ("name_ar", "name_en", "name_ms")
    list_editable = ("is_recommended", "status")


@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image_url", "status")
    list_filter = ("status",)


@admin.register(SmallBanner)
class SmallBannerAdmin(admin.ModelAdmin):
    list_display = ("id", "image_url", "status")
    list_filter = ("status",)


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ("id", "image_url", "status")
    list_filter = ("status",)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image_url", "status")
    list_filter = ("status",)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "video_url", "status")
    list_filter = ("status",)


@admin.register(PromotionCategory)
class PromotionCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name_en", "status")
    list_filter = ("status",)
    search_fields = ("name_ar", "name_en", "name_ms")


@admin.register(PromotionProduct)
class PromotionProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_en",
        "category",
        "price",
        "promo_price",
        #"is_recommended",
        "status",
    )
    list_filter = ("status", "category")
    search_fields = ("name_ar", "name_en", "name_ms")



