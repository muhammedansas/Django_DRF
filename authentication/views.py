from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RegisterSerializer,LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.

class RegistrationApi(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:    
            return Response({"message":serializer.errors},status=status.HTTP_404_NOT_FOUND)
        return Response({"message":"User created"},status=status.HTTP_201_CREATED)
        

class LoginApi(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if serializer.is_valid():
            user = authenticate(username = serializer.data['username'],password = serializer.data['password'])
        else:
            return Response({"messages":serializer.errors},status=status.HTTP_404_NOT_FOUND)

        if not user:
            return Response({"message":"invalid"},status=status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"message":"Login success","token":str(token)},status=status.HTTP_201_CREATED)
