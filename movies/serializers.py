# from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from reviews.models import Review
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


# class MovieSerializer(serializers.Serializer):
#    id = serializers.IntegerField()
#    title = serializers.CharField()
#    genre = serializers.PrimaryKeyRelatedField(
#        queryset=Genre.objects.all()
#    )
#    release_date = serializers.DateField()
#    actors = serializers.PrimaryKeyRelatedField(
#        queryset=Actor.objects.all(),
#        many=True,
#    )
#    resume = serializers.CharField()
#
#    def create(self, validated_data):
#
#        actors_data = validated_data.pop('actors')  # SEPARAMOS O ACTORS POR SER MANYTOMANY (BOAS PRATICAS)
#        new_movie = Movie.objects.create(
#            title=validated_data['title'],
#            genre=validated_data['genre'],       # RECEBEMOS O DICIONARIO DO POST EM VALIDATED_DATA E SALVAMOS COM CREATE()
#            release_date=validated_data['release_date'],
#            resume=validated_data['resume']
#        )
#        new_movie.actors.set(actors_data)  # DEPOIS DE SALVO, AI ADICIONAMOS O ACTORS
#        return new_movie
#
#    def update(self, instance, validated_data):
#        # ESSE METODO DO VALIDATED_DATA.GET() RECEBE 2 PARAMETROS
#        # E O MOTIVO É QUE ATUALIZAREMOS NOSSO BANCO DE DADOS SEM TER O PERIGO DE RECEBER UM NONE
#        # ENTÃO MESMO SE NAO DIGITAR UM CAMPO NULL LA NO PUT, ELE CONTINUA COM O REGISTRO EXISTENTE
#        instance.title = validated_data.get('title', instance.title)
#        instance.genre = validated_data.get('genre', instance.genre)
#        instance.release_date = validated_data.get('release_date', instance.release_date)
#        instance.resume = validated_data.get('resume', instance.resume)
#        actors_data = validated_data.get('actors')
#        if actors_data:
#            instance.actors.set(actors_data)  # aqui continua o mesmo de create, serve para salvar depois o actors
#        instance.save()
#        return instance
#
#    def delete(self, validate_data):
#        id = validate_data.get('id')
#
#        movie = Movie.objects.filter(id=id)
#        movie_name = movie['title']
#        movie.delete()
#        return {'message': f'filme {movie_name} excluido com sucesso'}


class MovieListDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'rate', 'release_date', 'resume']

    def get_rate(self, obj):
        '''METODO COM AGGREGATE E AVG'''
        # rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        # if rate:
        #    return round(rate, 1)
        # return None
        '''METODO COM QUERYSET E LIST COMPREHENSION'''
        notas = Review.objects.filter(movie=obj.id)
        review = sum([nota.stars for nota in notas])
        if review > 0:
            return round(review / len(notas), 1)
        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
    total_actors = serializers.IntegerField()


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('O ano precisa ser maior ou igual que 1990')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('ERRO: você ultrapassou o limite de 500 caracteres')
        return value
