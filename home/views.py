from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Persons,Workers
from .serializer import Personserialzer,Workerserialzer
from rest_framework.views import APIView
from rest_framework import viewsets,status
from django.contrib.auth.models import AbstractUser

# Create your views here.


# normal View sets in DRF:
# /////////////////////////////////////////////////////////////////////////////////
class NormalViewSets(viewsets.ViewSet):
    def list(self,request):
        PersonObj = Persons.objects.all()
        serializer = Personserialzer(PersonObj, many = True)
        return Response(serializer.data)



# Model view sets:
# ////////////////////////////////////////////////////////////////////////////////

class Modelviewsets(viewsets.ModelViewSet):
    serializer_class = Personserialzer
    queryset = Persons.objects.all()

    def list(self,request):
        search = request.GET.get('search')
        queryset = self.queryset

        if search:
            queryset = queryset.filter(name__startswith = search)

        serializer = Personserialzer(queryset,many = True)
        return Response(serializer.data)    



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
    
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def workers(request):
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

        