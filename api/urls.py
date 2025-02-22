from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('singers', views.SingerViewSet)  
router.register('songs', views.SongViewSet)  

urlpatterns = [
    path('', include(router.urls)),
]

