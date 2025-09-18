from rest_framework import serializers

from .models import Listing


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    seller = serializers.HyperlinkedRelatedField(
        view_name="user-detail",
        lookup_field="username",
        read_only=True
    )

    class Meta:
        model = Listing
        fields = [
            "url",
            "id",
            "title",
            "price",
            "description",
            "image_url",
            "active",
            "created_at",
            "seller",
        ]
