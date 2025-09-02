"""Module docstring."""

from rest_framework import serializers

from .models import Realtor


class RealtorSerializer(serializers.ModelSerializer):
    """Realtor serializer."""

    class Meta:
        """Meta class."""

        model = Realtor
        fields = "__all__"
