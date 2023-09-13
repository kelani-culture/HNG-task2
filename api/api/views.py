from rest_framework import status
from rest_framework.response import Response
from .serializer import User
from rest_framework.decorators import api_view
from .serializer import UserSerializer
"""
    create an API that perform CRUD on the client
    request data
"""


@api_view(['POST'])
def api(request):

    """
    Performs the Create part of the o based on client requests
    and return expected response
    """
    # Create based on client request 
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def api_RUD(request, id):
    """
        Performs the RUD operation based on client
        request and sending corresponding respond
    """
    
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Retrieve based on client request
    if request.method == "GET":
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

    # Update based on client request    
    elif request.method == "PUT":
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response(user_serializer.data)
        
    # delete based on client request
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)