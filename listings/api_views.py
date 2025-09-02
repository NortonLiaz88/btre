"""Module docstring."""

from rest_framework import filters, generics
from rest_framework.pagination import PageNumberPagination

from .models import Listing
from .serializers import ListingSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """Standard results set pagination."""
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class Listings(generics.ListCreateAPIView):
    """Listings view."""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "city", "state", "zipcode"]


class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    """Listing detail view."""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
