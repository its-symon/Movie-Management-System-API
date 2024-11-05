from django.urls import path
from movie.api.views import (MovieRatingListView, MovieRatingCreateView, MovieRatingDetailView) 

urlpatterns = [

    # Movie Rating URLs / Endpoints
    path('<int:pk>/rating/', MovieRatingListView.as_view(), name='movie-rating'),
    path('<int:pk>/rating-create/', MovieRatingCreateView.as_view(), name='rating-create'),
    path('rating/<int:pk>/', MovieRatingDetailView.as_view(), name='movie-rating'),
]