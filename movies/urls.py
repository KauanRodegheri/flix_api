from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-update-delete'),
    # path('movies/stats/<int:pk>/', views.movie_estatistics, name='estatistics'),
    path('movies/stats/', views.MovieStatesView.as_view())
]
