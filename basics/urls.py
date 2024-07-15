from django.urls import path
from . import views

urlpatterns = [
    path('student_details/',views.student_details,name="student_details"),
    path('student_allDetails/',views.student_allDetails,name="student_allDetails"),
]
