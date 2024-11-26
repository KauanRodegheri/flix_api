
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from django.http import JsonResponse
from movies.models import Movie
from movies.serializers import MovieModelSerializer


class MovieCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

class MovieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    
    def delete(self, request, pk,*args, **kwargs):
        movies = Movie.objects.all()
        movie = [movie.title for movie in movies if movie.id==pk]
        super().delete(request, *args, **kwargs)
        return JsonResponse(
            {"message": f'the movie {movie[0]} is deleted'}
        )