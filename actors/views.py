import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from actors.models import Actor
from actors.serializers import ActorSerializer

class ActorCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


    
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'message': f"actor delete success"})
    
'''USANDO FUNCTION BASED VIEWS ( GET E POST )'''    
#@csrf_exempt
#def actor_create_list_view(request):
#
#    if request.method == 'GET':
#        actors = Actor.objects.all()
#        data = [
#            {
#                'id': actor.id,
#                'name': actor.name,
#                'birthday': actor.birthday,
#                'nationality': actor.nationality
#            }
#            for actor in actors
#        ]
#        return JsonResponse(
#            data, safe=False
#        )
#    
#    elif request.method == 'POST':
#        data = json.loads(request.body.decode('utf-8'))
#        actor = Actor(
#            name=data['name'],
#            birthday=data['birthday'],
#            nationality=data['nationality']
#        )
#        actor.save()
#        return JsonResponse(
#            {
#                'id': actor.id,
#                'name': actor.name,
#                'birthday': actor.birthday,
#                'nationality': actor.nationality
#            },
#            status=201 
#        )

'''USANDO FUNCTION BASED VIEWS (GET, PUT E DELETE)'''
#@csrf_exempt   
#def actor_retrieve_update_detroy_view(request, pk):
#    actor = get_object_or_404(Actor, pk=pk)
#
#    if request.method == 'GET':
#        return JsonResponse(
#            {
#                'id': actor.id,
#                'name': actor.name,
#                'birthday': actor.birthday,
#                'nationality': actor.nationality
#            }
#        )
#    elif request.method == 'PUT':
#        data = json.loads(request.body.decode('utf-8'))
#        actor.name, actor.birthday, actor.nationality = data['name'], data['birthday'], data['nationality']
#        actor.save()
#        return JsonResponse(
#            {
#                'id': actor.id,
#                'name': actor.name,
#                'birthday': actor.birthday,
#                'nationality': actor.nationality
#            }
#        )
#    elif request.method == 'DELETE':
#        actor.delete()
#        return JsonResponse(
#            {
#                'name': actor.name,
#                'birthday': actor.birthday,
#                'nationality': actor.nationality
#            }
#        )

        



