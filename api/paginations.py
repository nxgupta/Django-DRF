from rest_framework import pagination
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    page_query_param = 'page-num'
    max_page_size = 2
    page_size = 4


    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_size': len(data),
            'results': data
        })