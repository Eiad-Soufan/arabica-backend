from django.urls import path
from .views import *

urlpatterns = [
    path("hero-images/", HeroImageListAPIView.as_view(), name="hero-images"),

    path("recommended-products/", RecommendedProductListAPIView.as_view(), name="recommended-products"),

    path("small-banners/", SmallBannerListAPIView.as_view(), name="small-banners"),

    # NORMAL CATEGORIES
    path("categories/", CategoryListAPIView.as_view(), name="categories"),
    path("products/", ProductListAPIView.as_view(), name="products"),
    path("categories/<int:category_id>/products/", CategoryProductsListAPIView.as_view(), name="category-products"),

    # PROMOTIONS (old banners)
    path("promotions/", PromotionListAPIView.as_view(), name="promotions"),

    # ✅ NEW PROMOTION CATEGORIES
    path("promotion-categories/", PromotionCategoryListAPIView.as_view(), name="promotion-categories"),

    # ✅ NEW PROMOTION PRODUCTS
    path("promotion-products/", PromotionProductListAPIView.as_view(), name="promotion-products"),
    path(
        "promotion-categories/<int:category_id>/products/",
        PromotionCategoryProductsListAPIView.as_view(),
        name="promotion-category-products",
    ),

    path("gallery-images/", GalleryImageListAPIView.as_view(), name="gallery-images"),
    path("videos/", VideoListAPIView.as_view(), name="videos"),

    path("__backup__/dump/", export_database),
]
