# Vendor
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
# Local
from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    """Отзыв"""
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
