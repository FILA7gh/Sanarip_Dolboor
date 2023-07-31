from rest_framework.pagination import PageNumberPagination


class PaginationForTen(PageNumberPagination):
    page_size = 10
