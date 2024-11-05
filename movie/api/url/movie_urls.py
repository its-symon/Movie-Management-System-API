from django.urls import path
from movie.api.views import ( MovieListView, MovieCreateView, MovieDetailView) 

urlpatterns = [
    # Movie URLs / Endpoints
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movie-create/', MovieCreateView.as_view(), name='movie-create'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
]