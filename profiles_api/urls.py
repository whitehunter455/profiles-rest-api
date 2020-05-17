from django.urls import path
from profiles_api import views

#Section ViewSet
from django.urls import include
from rest_framework.routers import DefaultRouter

#Created for ViewSet
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
#===========================

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), #http://127.0.0.1:8000/api/hello-view/
    path('', include(router.urls)), #http://127.0.0.1:8000/api/
]
