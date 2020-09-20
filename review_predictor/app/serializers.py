# Vendor
from rest_framework import serializers
# Local
from .models import Review
from review_predictor.app.reviews import predict_rating


class ReviewSerializer(serializers.ModelSerializer):
    """Базовый сериалайзер для отзывов"""
    class Meta:
        model = Review
        fields = ["id", "text", "rating", "created_at"]
        read_only_fields = ["id", "rating", "created_at"]
        extra_kwargs = {'text': {'allow_null': False}}

    def create(self, validated_data):
        text = validated_data.get('text')
        validated_data['rating'] = predict_rating(text)
        return super().create(validated_data)
