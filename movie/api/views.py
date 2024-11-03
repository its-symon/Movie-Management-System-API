from django.shortcuts import redirect, get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import ValidationError

from movie.models import Movie, Rating, Report
from .serializers import MovieSerializer, RatingSerializer, ReportSerializer



# Movie Views
class MovieListView(generics.ListAPIView):
    """
    API endpoint that allows users to view all movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = []

class MovieCreateView(generics.CreateAPIView):
    """
    API endpoint that allows users to view all movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to view a specific movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    

# Rating Views
class MovieRatingListView(generics.ListAPIView):
    """
    API endpoint that allows users to view all ratings for a specific movie.
    """
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Rating.objects.filter(movie_id=pk)
    
class MovieRatingCreateView(generics.CreateAPIView):
    """
    API endpoint that allows users to create a new rating for a specific movie.
    """
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        movie_id = self.kwargs['pk']
        movie = Movie.objects.get(pk=movie_id)

        rating_user = Rating.objects.filter(user=user, movie=movie)
        if rating_user.count() > 0:
            raise ValidationError('You have already rated this movie')
    
        serializer.save(user=user, movie=movie)

    
class MovieRatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to view a specific movie rating.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]


# Report Views
class MovieReportListView(generics.ListAPIView):
    """
    API endpoint that allows users to view all reports for a specific movie.
    """
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Report.objects.filter(movie_id=pk)
    

class MovieReportCreateView(generics.CreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        movie_id = self.kwargs['pk']
        user = self.request.user

        movie = Movie.objects.get(id=movie_id)
        report = Report.objects.filter(user=user, movie=movie)

        if report.count() > 0:
            raise ValidationError('You have already reported this movie')

        serializer.save(user=user, movie=movie)


class MovieReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to view a specific movie report.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]


# Admin reports views

class AdminReportListView(generics.ListAPIView):
    """
    API endpoint that allows administrators to view all reports.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser] 


# class AdminReportApprove(generics.CreateAPIView):
#     """
#     API endpoint that allows administrators to approve a specific report.
#     """
#     serializer_class = ReportSerializer
#     permission_classes = [IsAdminUser]
#     queryset = Report.objects.all()
    
#     def perform_create(self, serializer):
#         report_id = self.kwargs['pk']
#         report = get_object_or_404(Report, id=report_id)
#         report.is_approved = True
#         report.save()