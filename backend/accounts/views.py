from django.contrib.auth import get_user_model
from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserSerializer


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MeView(views.APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
