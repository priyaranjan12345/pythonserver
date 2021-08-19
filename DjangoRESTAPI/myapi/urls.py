from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import cars_list, car_details, CarAPIView, CarDetails, GenericAPIView, CarGenerics, CarViewSet

router = DefaultRouter()
router.register('cars', CarViewSet, basename='carview')

urlpatterns = [
    path('carlist/', cars_list),
    path('cardetail/<int:pkey>/', car_details),

    path('carapiview/', CarAPIView.as_view()),
    path('carapiview/<int:id>/', CarDetails.as_view()),
    
    path('genericapiview/', GenericAPIView.as_view()),
    path('genericapiview/<int:id>/', CarGenerics.as_view()),

    path('carviewset/', include(router.urls)),
]
