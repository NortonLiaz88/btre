"""Module docstring."""

from rest_framework import filters, generics

from listings.api_views import StandardResultsSetPagination

from .models import Realtor
from .serializers import RealtorSerializer


class Realtors(generics.ListCreateAPIView):
    """Realtors view."""
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class RealtorDetail(generics.RetrieveUpdateDestroyAPIView):
    """Realtor detail view."""
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
