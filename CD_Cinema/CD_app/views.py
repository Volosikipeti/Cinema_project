from django.shortcuts import render
from .models import Genre, Movie


def home_page(request):
    return render(request, "./movies/index.html")

def top_movies_page(request):
    return render(request, "./movies/top-movies.html")

def all_movies_page(request):
    return render(request, "./movies/all-movies.html")

def movie_detail_page(request):
    return render(request, "./movies/movie-detail.html")

def movies_by_category_page(request):
    return render(request, "./movies/movies-by-category.html")

def movies_by_search_page(request):
    return render(request, "./movies/movies-by-search.html")
