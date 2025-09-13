from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            # accounts
            "register": reverse('register', request=request, format=format),
            "login": reverse('login', request=request, format=format),
            "refresh": reverse('token-refresh', request=request, format=format),
            "me": reverse('me', request=request, format=format),
            
            # listings
            "listings": reverse('listing-list', request=request, format=format),
        }
    )
