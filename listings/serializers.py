"""Module docstring."""

from rest_framework import serializers

from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    """Listing serializer."""

    class Meta:
        """Meta class."""

        model = Listing
        fields = "__all__"
