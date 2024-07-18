from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RegisterSerializer,LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class RegistrationApi(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:    
            return Response({"message":serializer.errors},status=status.HTTP_404_NOT_FOUND)
        return Response({"message":"User created"},status=status.HTTP_201_CREATED)
        

class LoginApi(APIView):
    permission_classes=[AllowAny]

    
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









class Loginview(APIView):
    permission_classes = [AllowAny]
    @method_decorator(csrf_exempt)
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"detail": "Successfully logged in."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)