from django.urls import path
from . import views

urlpatterns =[
    path('', views.home_page, name='home_page'),
    path('movies/top/', views.top_movies_page, name='top_movies_page'),
    path('movies/all/', views.all_movies_page, name='all_movies_page'),
    path('movies/detail/', views.movie_detail_page, name='movie_detail_page'),
    path('movies/category/', views.movies_by_category_page, name='movies_by_category_page'),
    path('movies/search/', views.movies_by_search_page, name='movies_by_search_page'),
]