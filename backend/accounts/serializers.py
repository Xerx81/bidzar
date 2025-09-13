from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    listings = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="listing-detail",
        read_only=True,
        lookup_field="pk"
    )

    email = serializers.EmailField(write_only=False, required=False)

    class Meta:
        model = User
        fields = ["url","id", "username", "email", "password", "listings"]
        extra_kwargs = {
            "url": {"view_name": "user-detail", "lookup_field": "username"},
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user

    def to_representation(self, instance):
        # Only show email if the looged in user is the same as profile owner
        data = super().to_representation(instance)
        request = self.context.get("request")
        if request and request.user != instance:
            data.pop("email")
        return data
