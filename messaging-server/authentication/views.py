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

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    def post(self, request):
        data = request.data 
        usernameOrEmail = data.get('usernameOrEmail', '')
        password = data.get('password')
        user = authenticate(username=usernameOrEmail, password=password)

        #return user info if authenticated
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'userId': user.pk,
                'email': user.email,
                'username': user.username,
                'dateJoined': user.date_joined
            })
       
        #Return why user was not authenticated, email or username not found or the password was incorrect
        if User.objects.filter(email=usernameOrEmail).exists() or User.objects.filter(username=usernameOrEmail).exists():
                return Response({'Incorrect password': 'Password provided is incorect'},  status=status.HTTP_401_UNAUTHORIZED)

        return Response({'Account not found': 'Account with such email or username was not found'},
                            status=status.HTTP_401_UNAUTHORIZED)

            
        
   