from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from .models import Persons,Workers
from .serializer import Personserialzer,Workerserialzer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import viewsets,status
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import logout
from .CustomePermissions import Mypermission
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core import paginator


# Create your views here.


# normal View sets in DRF:
# /////////////////////////////////////////////////////////////////////////////////
class NormalViewSets(viewsets.ViewSet):
    def list(self,request):
        PersonObj = Persons.objects.all()
        page = request.GET.get('page',1)
        page_size = 2
        paginater = paginator(PersonObj,page_size)
        serializer = Personserialzer(paginater.page(page), many = True)
        return Response(serializer.data)
    


# pagination:
# /////////////////////////////////////////////////////////////////////////////////
class customPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page'


# Model view sets:
# ////////////////////////////////////////////////////////////////////////////////

class Modelviewsets(viewsets.ModelViewSet):
    serializer_class = Personserialzer
    queryset = Persons.objects.all()
    pagination_class = customPagination
    

    def list(self,request):
        search = request.GET.get('search')
        queryset = self.queryset
        

        if search:
            queryset = queryset.filter(name__startswith = search)

        paginated_queryset = self.paginate_queryset(queryset)    

        serializer = Personserialzer(paginated_queryset,many = True)
        return self.get_paginated_response({"status":200,"data":serializer.data})    

class Logout(APIView):
    def post(self,request):
        logout(request)
        return Response({"message":"sucessfully logout"})

# class based APIview method:
# //////////////////////////////////////////////////////////////////////////////////
class ClassBaseView(APIView):
    def get(self,request):
        PersonObj = Persons.objects.all()
        serializer = Personserialzer(PersonObj, many = True)
        return Response(serializer.data)

    def post(self,request):
        return Response("this class based view post method")

# function based APIview method:
# //////////////////////////////////////////////////////////////////////////////////////
@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        people_details = {
            'name':'ansas',
            'age':21,
            'place':'kozhikode'
        }
        return Response(people_details)
    elif request.method == 'POST':
        print("this is post")
        return Response("This is POST method")
    
@authentication_classes([JWTAuthentication])
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        PersonObj = Persons.objects.all()
        serializer = Personserialzer(PersonObj, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = Personserialzer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        SingleObj = Persons.objects.get(id = data['id'])
        serializer = Personserialzer(SingleObj,data=data,partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PATCH":
        data = request.data
        SingleObj = Persons.objects.get(id = data['id'])
        serializer = Personserialzer(SingleObj,data=data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
@permission_classes([Mypermission])  
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def workers(request):
    print(request.method,'lllllllll')
    if request.method == 'GET':
        obj = Workers.objects.all()
        serializer = Workerserialzer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        serializer = Workerserialzer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = Workers.objects.get(id=data['id'])
        serializer = Workerserialzer(obj,data=data, partial = False)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = Workers.objects.get(id = data['id'])
        serializer = Workerserialzer(obj,data=data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        data = request.data
        obj = Workers.objects.get(id = data['id'])
        obj.delete()
        return Response({"message":"data has deleted"})

        