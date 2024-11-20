import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Genre
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



#@csrf_exempt
#def genre_create_list_view(request):
#    if request.method == 'GET':
#        genres = Genre.objects.all()
#        data = [{'id': genre.id, 'genero': genre.name} for genre in genres]
#        return JsonResponse(
#            data,
#            safe=False
#        )
#    elif request.method == 'POST':
#        data = json.loads(request.body.decode('utf-8'))
#        new_genre = Genre(name=data['name'])
#        new_genre.save()
#        return JsonResponse(
#            {'id': new_genre.id, 'genero': new_genre.name},
#            status=201,
#        )

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    

#@csrf_exempt
#def genre_detail_view(request, pk):
#    genre = get_object_or_404(Genre, id=pk)
#    match request.method:
#        
#        case 'GET':
#            data = {'id': genre.id, 'genero': genre.name}
#            return JsonResponse(
#                data
#            )
#    
#        case 'PUT':
#            data = json.loads(request.body.decode('utf-8'))
#            genre.name = data['name']
#            genre.save()
#            return JsonResponse(
#                {'id': genre.id, 'genero': genre.name}
#            )
#    
#        case 'DELETE':
#            genre.delete()
#            return JsonResponse(
#                {'message': f'genêro {genre.name} excluido com sucesso'},
#                status=204,
#            )