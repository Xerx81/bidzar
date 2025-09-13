from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    listings = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="listing-detail",
        read_only=True,
        lookup_field="pk"
    )

    class Meta:
        model = User
        fields = ["url","id", "username", "email", "password", "listings"]
        extra_kwargs = {
            "url": {"view_name": "user-detail", "lookup_field": "username"}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
