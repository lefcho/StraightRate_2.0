from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from StraightRate_2.reviews.models import MovieReview, VideoGameReview


class MovieReviewSerializer(ModelSerializer):
    user = StringRelatedField(read_only=True)
    like_count = serializers.IntegerField(source='likes.count', read_only=True)
    liked = serializers.SerializerMethodField()

    class Meta:
        model = MovieReview
        fields = '__all__'
        read_only_fields = ['user', 'last_edited']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False


class VideoGameReviewSerializer(ModelSerializer):
    user = StringRelatedField(read_only=True)
    like_count = serializers.IntegerField(source='likes.count', read_only=True)
    liked = serializers.SerializerMethodField()
    class Meta:
        model = VideoGameReview
        fields = '__all__'
        read_only_fields = ['user', 'last_edited']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False
