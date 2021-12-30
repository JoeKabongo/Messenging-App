from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer


class SignupView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(formatSerializerErrors(serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    def post(self, request):
        data = request.data
        usernameOrEmail = data.get('usernameOrEmail', '')
        password = data.get('password')
        user = authenticate(username=usernameOrEmail, password=password)

        # return user info if authenticated
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'userId': user.pk,
                'email': user.email,
                'username': user.username,
                'dateJoined': user.date_joined
            })

        # Return why user was not authenticated, email or username not found or the password was incorrect
        if User.objects.filter(email=usernameOrEmail).exists() or User.objects.filter(username=usernameOrEmail).exists():
            return Response(
                {'errors':
                 [
                     {
                         'error': 'Authentication error',
                         'message': 'The password you’ve entered is incorrect'}

                 ]},  status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            'errors': [
                {'error': 'Authentication error',
                    'message': 'email or username you entered isn’t connected to an account'}
            ]
        }, status=status.HTTP_401_UNAUTHORIZED)


# TODO: will need to move this where it can be reused by other views in the future
def formatSerializerErrors(serializerErrors):
    """ 
        Format serializer error be consistant with others error responses format
        eg: {'username': ['Ensure this field has no more than 30 characters'] } -> 
        {'errors': [{'error': 'bad request'}, message: 'username: Ensure this field has no more than 30 characters']}
    """
    if serializerErrors.get('errors', None):
        return serializerErrors

    errors = []
    for key in serializerErrors:
        keyErrors = serializerErrors[key]
        for error in keyErrors:
            errors.append(
                {'error': 'Bad request', 'message': key + ": " + error})

    return {'errors': errors}
