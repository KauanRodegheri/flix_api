from rest_framework import serializers
from reviews.models import Review
from movies.serializers import MovieListDetailSerializer


class ReviewListDetailSerializer(serializers.ModelSerializer):
    movie = MovieListDetailSerializer()

    class Meta:
        model = Review
        fields = ['id', 'movie', 'stars', 'comments']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
