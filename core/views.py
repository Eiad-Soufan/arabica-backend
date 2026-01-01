from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
from .pagination import StandardResultsSetPagination





class HeroImageListAPIView(ListAPIView):
    serializer_class = HeroImageSerializer

    def get_queryset(self):
        return HeroImage.objects.filter(status="published").order_by("id")



class RecommendedProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(
            status="published",
            is_recommended=True
        ).order_by("id")



class SmallBannerListAPIView(ListAPIView):
    serializer_class = SmallBannerSerializer

    def get_queryset(self):
        return SmallBanner.objects.filter(
            status="published"
        ).order_by("id")





class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(status="published").order_by("id")


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Product.objects.filter(status="published").order_by("id")


class CategoryProductsListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return Product.objects.filter(
            status="published",
            category_id=category_id
        ).order_by("id")



class PromotionListAPIView(ListAPIView):
    serializer_class = PromotionSerializer

    def get_queryset(self):
        return Promotion.objects.filter(status="published").order_by("id")


class GalleryImageListAPIView(ListAPIView):
    serializer_class = GalleryImageSerializer

    def get_queryset(self):
        return GalleryImage.objects.filter(status="published").order_by("id")


class VideoListAPIView(ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.filter(status="published").order_by("id")