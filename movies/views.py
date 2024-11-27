from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from django.http import JsonResponse
from movies.models import Movie
from movies.serializers import MovieModelSerializer
from django.shortcuts import get_object_or_404
from reviews.models import Review
from actors.models import Actor
from django.db.models import Count, Avg

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
    
class MovieStatesView(views.APIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]
    queryset = Movie.objects.all()

    def get(self, request):
        '''buscar dados'''
        #TOTAL DE FILMES
        total_movies = self.queryset.count()
        #TOTAL DE FILMES POR GENEROS
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        lista=[]
        for item in movies_by_genre:
            lista.append({'genero': item['genre__name'], 'count': item['count']})
        #TOTAL DE REVIEWS E MEDIA DE ESTRELAS
        total_reviews = Review.objects.all().count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        total_actors = Actor.objects.all().count()
        '''MONTAR A RESPOSTA'''
        data = {'toal_movies': total_movies,
                'movies_by_genre': lista,
                'total_reviews': total_reviews,
                'average_stars': round(average_stars, 1) if average_stars else 0,
                'total_actors': total_actors
            }
        
        '''RETORNAR A RESPOSTA'''
        return response.Response(
            data,
            status=status.HTTP_200_OK
        )
    