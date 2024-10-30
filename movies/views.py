
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieCreateListView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer