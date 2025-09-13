from rest_framework import serializers

from .models import Listing


class ListingsSerializer(serializers.HyperlinkedModelSerializer):
    seller = serializers.ReadOnlyField(source="seller.username")

    class Meta:
        model = Listing
        fields = ["url", "id", "title", "price", "description", "image_url", "active", "created_at", "seller"]
