from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from StraightRate_2.reviews.models import MovieReview


class MovieReviewSerializer(ModelSerializer):
    user = StringRelatedField(read_only=True)

    class Meta:
        model = MovieReview
        fields = '__all__'
        read_only_fields = ['user', 'last_edited']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
