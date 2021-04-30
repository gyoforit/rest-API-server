from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/review/', views.create_review),
    path('review/<int:review_pk>/', views.review_detail),
    path('review/<int:review_pk>/comment/', views.create_comment),
    path('review/<int:review_pk>/comment/<int:comment_pk>/', views.comment_detail),
    path('createdata/', views.create_data),
]
