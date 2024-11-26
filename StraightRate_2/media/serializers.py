from rest_framework import serializers
from StraightRate_2.media.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    directors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
