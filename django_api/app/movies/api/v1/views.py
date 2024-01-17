from rest_framework import generics, serializers

from movies.models import FilmWork

from movies.models import Person, Genre
from .serializers import FilmWorkSerializer


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class FilmWorkList(generics.ListAPIView):
    queryset = FilmWork.objects.all()
    serializer_class = FilmWorkSerializer


class FilmWorkDetail(generics.RetrieveAPIView):
    queryset = FilmWork.objects.all()
    serializer_class = FilmWorkSerializer
