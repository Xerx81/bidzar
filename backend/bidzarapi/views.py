from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response(
        {
            # accounts
            "register": reverse('register', request=request, format=format),
            "login": reverse('login', request=request, format=format),
            "refresh": reverse('token-refresh', request=request, format=format),
            
            # listings
            "listings": reverse('listing-list', request=request, format=format),
        }
    )
