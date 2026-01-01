# core/pagination.py

from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    # ?page=1
    page_size = 12  # default
    page_size_query_param = "page_size"  # allow override: ?page_size=24
    max_page_size = 50
