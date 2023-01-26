from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "size"
    page_size = 5
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('maxsize', self.max_page_size),
            ('page', self.page.number),
            ('size', self.page.paginator.per_page),
            ('num_pages', self.page.paginator.num_pages),
            ('results', data)
        ]))

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 123,
                },
                'maxsize': {
                    'type': 'integer',
                    'example': 123,
                },
                'page': {
                    'type': 'integer',
                    'example': 123,
                },
                'size': {
                    'type': 'integer',
                    'example': 123,
                },
                'num_pages': {
                    'type': 'integer',
                    'example': 123,
                },
                'results': schema,
            },
        }