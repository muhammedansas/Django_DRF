from django.urls import path,include
from home import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('person/',views.person,name='person'),
    path('classbasedview/',views.ClassBaseView.as_view(),name='classbasedview'),
]