# Vendor
from django.urls import path
# Local
from .views import ReviewViewSet


urlpatterns = [
    path(
        'reviews/',
        ReviewViewSet.as_view({'post': 'create', 'get': 'list'}),
        name='reviews'
    )
]
