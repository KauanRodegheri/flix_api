
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from movies.models import Movie
from movies.serializers import MovieSerializer
from django.http import JsonResponse

class MovieCreateListView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def delete(self, request, pk,*args, **kwargs):
        movies = Movie.objects.all()
        movie = [movie.title for movie in movies if movie.id==pk]
        super().delete(request, *args, **kwargs)
        return JsonResponse(
            {"message": f'the movie {movie[0]} is deleted'}
        )