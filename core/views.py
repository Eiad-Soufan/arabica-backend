from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
from .pagination import StandardResultsSetPagination


import json
import subprocess
import tempfile
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
@require_GET
def export_database(request):
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        subprocess.check_call([
            "python",
            "manage.py",
            "dumpdata",
            "--natural-foreign",
            "--natural-primary",
            "-e", "contenttypes",
            "-e", "auth.Permission",
            "--indent", "2",
        ], stdout=open(tmp_path, "w"))

        with open(tmp_path, "rb") as f:
            response = HttpResponse(
                f.read(),
                content_type="application/json"
            )
            response["Content-Disposition"] = 'attachment; filename="database_dump.json"'
            return response

    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)



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
