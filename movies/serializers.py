from .models import Movie, Review, Comment
from rest_framework import serializers

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title', 'release_date',)


class MovieSerializer(serializers.ModelSerializer):
    
    #review_count = serializers

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'release_date', 'poster_path', ) #'review_count', )


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content', 'rank', 'movie',)

        read_only_fields = ('movie',)


