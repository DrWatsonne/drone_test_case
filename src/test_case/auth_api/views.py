from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def token_test(request):
    if request.user.is_authenticated:
        return Response({'message': 'Authenticated user.'})
    return Response({'message': 'Not authenticated user.'})
