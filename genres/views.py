import json
from django.http import JsonResponse
from genres.models import Genre
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'genero': genre.name} for genre in genres]
        return JsonResponse(
            data,
            safe=False
        )
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse(
            {'id': new_genre.id, 'genero': new_genre.name},
            status=201,
        )

@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, id=pk)

    if request.method == 'GET':
        data = {'id': genre.id, 'genero': genre.name}
        return JsonResponse(
            data
        )
    
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            {'id': genre.id, 'genero': genre.name}
        )
    
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            {'message': f'genêro {genre.name} excluido com sucesso'},
            status=204,
        )


    
