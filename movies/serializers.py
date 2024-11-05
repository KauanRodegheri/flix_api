from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all()
    )
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True,
    )
    resume = serializers.CharField()

    def create(self, validated_data):

        actors_data = validated_data.pop('actors')
        new_movie = Movie.objects.create(
            title = validated_data['title'],
            genre = validated_data['genre'],
            release_date = validated_data['release_date'],
            resume = validated_data['resume']
        )
        new_movie.actors.set(actors_data)
        return new_movie
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.resume = validated_data.get('resume', instance.resume)
        actors_data = validated_data.get('actors')
        if actors_data: instance.actors.set(actors_data)
        instance.save()
        return instance
    
    def delete(self, validate_data):
        id = validate_data.get('id')

        movie = Movie.objects.filter(id=id)
        movie_name = movie['title']
        movie.delete()
        return {'message': f'filme {movie_name} excluido com sucesso'}

class MovieModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'