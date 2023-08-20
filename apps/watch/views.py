from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Watch, WatchCategory, Review
from .paginations import StandardResultsSetPagination
from .serializers import WatchSerializer, WatchCategorySerializer, ReviewSerializer
from rest_framework.filters import SearchFilter

class WatchViewSet(viewsets.ModelViewSet):
    queryset = Watch.objects.all().prefetch_related('category').order_by('id')
    serializer_class = WatchSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ['brand', 'model']

class WatchCategoryViewSet(viewsets.ModelViewSet):
    queryset = WatchCategory.objects.all()
    serializer_class = WatchCategorySerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
