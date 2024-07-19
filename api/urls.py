from django.urls import path,include
from home import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = DefaultRouter()
router.register(r'person',views.Modelviewsets , basename='person')
urlpatterns = router.urls


urlpatterns = [
    path('ModelViewsets/',include(router.urls)),
    path('index/',views.index,name='index'),
    path('person/',views.person,name='person'),
    path('classbasedview/',views.ClassBaseView.as_view(),name='classbasedview'),
    path('noramlviewset/',views.NormalViewSets.as_view({'get':'list'}),name='noramlviewset'),
    path('workers/',views.workers,name='workers'),
    path('logout/',views.Logout.as_view(),name='logout'),
    path('get_token/',TokenObtainPairView.as_view(),name="get_token"),
    path('refresh_token/',TokenRefreshView.as_view(),name="refresh_token"),
    path('verify_token/',TokenVerifyView.as_view(),name="verify_token"),
]