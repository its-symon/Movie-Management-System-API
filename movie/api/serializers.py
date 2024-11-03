from rest_framework import serializers

from movie.models import Movie, Rating, Report
from accounts.api.serializers import UserSerializer


class MovieSerializer(serializers.ModelSerializer):
    
    average_rating = serializers.FloatField(read_only=True)
    total_ratings = serializers.FloatField(read_only=True)

    class Meta:
        model = Movie
        fields = [
             'title', 'description', 'released_at', 
            'duration_hours', 'duration_minutes', 'duration_seconds', 
            'genre', 'created_by', 'language', 'average_rating', 'total_ratings'
        ]

    

class RatingSerializer(serializers.ModelSerializer):

    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ['user', 'movie', 'rating', 'created_at']


class ReportSerializer(serializers.ModelSerializer):

    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Report
        fields = ['user', 'movie', 'reason']
