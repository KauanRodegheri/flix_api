from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTHENTICATION
    path('api/v1/', include('authentication.urls')),
    # GENRE
    path('api/v1/', include('genres.urls')),
    # ACTORS
    path('api/v1/', include('actors.urls')),
    # MOVIES
    path('api/v1/', include('movies.urls')),
    # REVIEWS
    path('api/v1/', include('reviews.urls')),
]
