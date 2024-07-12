from django.urls import path,include
from home import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'person',views.Modelviewsets , basename='person')
urlpatterns = router.urls


urlpatterns = [
    path('',include(router.urls)),
    path('index/',views.index,name='index'),
    path('person/',views.person,name='person'),
    path('classbasedview/',views.ClassBaseView.as_view(),name='classbasedview'),
    path('noramlviewset/',views.NormalViewSets.as_view({'get':'list'}),name='noramlviewset'),
]