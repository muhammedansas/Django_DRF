from django.shortcuts import render,HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

# complex data into json formate using json renderer 
# ////////////////////////////////////////////////////////////////////////////////////

def student_details(request):
    detail = Student.objects.get(id = 1)
    print(detail)
    serializer = StudentSerializer(detail)
    print(serializer,"aaaaaaaaaaaaaaaaaa")
    print(serializer.data,"bbbbbbbbbbbbbb")
    json_data = JSONRenderer().render(serializer.data)
    print(json_data,"ccccccccccc")
    return HttpResponse(json_data,content_type = 'application/json')


# to get all the details:
# /////////////////////////////////////////////////////////////////
def student_allDetails(request):
    detail = Student.objects.all()
    print(detail)
    serializer = StudentSerializer(detail,many = True)
    print(serializer,"aaaaaaaaaaaaaaaaaa")
    print(serializer.data,"bbbbbbbbbbbbbb")
    json_data = JSONRenderer().render(serializer.data)
    print(json_data,"ccccccccccc")
    return HttpResponse(json_data,content_type = 'application/json')
