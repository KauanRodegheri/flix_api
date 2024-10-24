from django.http import JsonResponse
from django.contrib import admin
from django.urls import path
from genres.views import *
from actors.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreListUpdateDeleteView.as_view(), name='genre-detail'),

    #ACTORS
    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-list-update-delete'),
]
