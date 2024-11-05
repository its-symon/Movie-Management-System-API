from django.urls import path
from movie.api.views import (MovieReportListView, MovieReportCreateView, MovieReportDetailView) 

urlpatterns = [

    # Movie Report URLs/ Endpoints 
    path('<int:pk>/report/', MovieReportListView.as_view(), name='movie-report'),
    path('<int:pk>/report-create/', MovieReportCreateView.as_view(), name='movie-report-create'),
    path('report/<int:pk>/', MovieReportDetailView.as_view(), name='movie-report-detail'),
]