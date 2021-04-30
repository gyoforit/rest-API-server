from .models import Movie, Review, Comment
from rest_framework import serializers

class MovieListSerializer(serializers.ModelSerializer):
    
    review_count = serializers.IntegerField(source='reviews.count', read_only=True)

    class Meta:
        model = Movie
        fields = ('title', 'release_date', 'review_count',)


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'release_date', 'poster_path',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content', 'review',)

        read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    
    movie = MovieListSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('title', 'content', 'rank', 'movie', 'comments',)

        read_only_fields = ('movie',)



