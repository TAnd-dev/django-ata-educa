from rest_framework.pagination import PageNumberPagination


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_suze_query_param = 'page_size'
    max_page_size = 50