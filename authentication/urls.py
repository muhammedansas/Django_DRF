from django.urls import path,include
from . import views

urlpatterns = [
    path('registration/',views.RegistrationApi.as_view(),name='registration'),
    path('login/',views.LoginApi.as_view(),name='login'),
    path('Loginview/',views.Loginview.as_view(),name='Loginview'),
]
