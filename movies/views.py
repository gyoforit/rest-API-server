from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer, CommentSerializer
from .models import Movie, Review, Comment

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)

        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)

@api_view(['POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie) 

        return Response(serializer.data, status=status.HTTP_201_CREATED)       



@api_view(['GET', 'PUT', 'DELETE']) # GET 조회, PUT 수정 , DELETE 삭제
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review) #조회라서 그냥 위에서 불러오면 된다.
        return Response(serializer.data)

    #삭제
    elif request.method == 'DELETE':
        review.delete()
        return Response({'id': review_pk}, status=status.HTTP_204_NO_CONTENT) # 몇번 아이디 삭제되었는 지 반환 #삭제가 되어서 내용이 없다.


    #PUT 수정
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_detail(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment) #조회라서 그냥 위에서 불러오면 된다.
    return Response(serializer.data)


    

