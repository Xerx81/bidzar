from rest_framework import serializers

from .models import Listing


class ListingsSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source="seller.username")

    class Meta:
        model = Listing
        fields = "__all__"
