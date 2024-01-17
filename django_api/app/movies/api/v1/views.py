from rest_framework import generics
from movies.models import FilmWork
from .serializers import FilmWorkSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'next': self.get_next_link(),
            'prev': self.get_previous_link(),
            'results': data
        })

    def get_next_link(self):
        if not self.page.has_next():
            return None
        return self.page.next_page_number()

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        return self.page.previous_page_number()


class FilmWorkList(generics.ListAPIView):
    queryset = FilmWork.objects.prefetch_related('genres', 'persons').all()
    serializer_class = FilmWorkSerializer
    pagination_class = CustomPageNumberPagination


class FilmWorkDetail(generics.RetrieveAPIView):
    queryset = FilmWork.objects.prefetch_related('genres', 'persons').all()
    serializer_class = FilmWorkSerializer
