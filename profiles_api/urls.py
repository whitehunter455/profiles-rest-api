from django.urls import path
from profiles_api import views

#Section ViewSet
from django.urls import include
from rest_framework.routers import DefaultRouter

#Created for ViewSet
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) #Tidak perlu base_name karena di ViewSet sudah ada query_set
# if you provide the query set then Django rest framework can figure out the name from the model that's assigned
router.register('feed', views.UserProfileFeedViewSet)
#===========================

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), #http://127.0.0.1:8000/api/hello-view/
    path('login/', views.UserLoginApiView.as_view()), #http://127.0.0.1:8000/api/login/
    path('', include(router.urls)), #http://127.0.0.1:8000/api/
]
