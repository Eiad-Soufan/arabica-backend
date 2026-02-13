from rest_framework import serializers
from .models import *

class HeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroImage
        fields = ["id", "image_url", "status"]



class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source="category.id", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "category_id",
            "name_ar",
            "name_en",
            "name_ms",
            "description_ar",
            "description_en",
            "description_ms",
            "price",
            "promo_price",
            "image_url",
            "is_recommended",
        ]


class SmallBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmallBanner
        fields = [
            "id",
            "image_url",
            "link",
        ]





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name_ar",
            "name_en",
            "name_ms",
            "image_url",
        ]


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ["id", "image_url", "link"]


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ["id", "image_url"]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video

        fields = ["id", "video_url"]


class PromotionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionCategory
        fields = [
            "id",
            "name_ar",
            "name_en",
            "name_ms",
            "image_url",
        ]


class PromotionProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source="category.id", read_only=True)

    class Meta:
        model = PromotionProduct
        fields = [
            "id",
            "category_id",
            "name_ar",
            "name_en",
            "name_ms",
            "description_ar",
            "description_en",
            "description_ms",
            "price",
            "promo_price",
            "image_url",
            "is_recommended",
        ]
