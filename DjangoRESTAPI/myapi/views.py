import re
from django.http import JsonResponse
from django.http import response
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.serializers import Serializer
from .models import Cars
from .serializers import CarsSerializers
from rest_framework.decorators import api_view
# Create your views here.
#type-2
@api_view(['GET', 'POST'])
def cars_list(request):
    if(request.method == 'GET'):
        cars = Cars.objects.all()
        serializer = CarsSerializers(cars, many=True)

        return Response(serializer.data)

    elif(request.method == 'POST'):
        d = JSONParser().parse(request)
        serializer = CarsSerializers(data=d)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#type-1
@csrf_exempt
def car_details(request, pkey):
    try:
        cars = Cars.objects.get(pk=pkey)
    except Cars.DoesNotExist:
        return HttpResponse(status=404)

    if(request.method == 'GET'):
        serializer = CarsSerializers(cars)

        return JsonResponse(serializer.data)

    elif(request.method == 'PUT'):
        d = JSONParser().parse(request)
        serializer = CarsSerializers(cars, data=d)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif(request.method == 'DELETE'):
        cars.delete()
        return HttpResponse(status=204)

#type-3
from rest_framework.views import APIView

class CarAPIView(APIView):
    def get(self, request):
        cars = Cars.objects.all()
        serializer = CarsSerializers(cars, many=True)

        return Response(serializer.data)

    def post(self, request):
        cardata = request.data
        serializer = CarsSerializers(data = cardata)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetails(APIView):
    def get_object(self, id):
        try:
            return Cars.objects.get(id=id)
        except Cars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id=None):
        car = self.get_object(id)
        serializer = CarsSerializers(car)
        return Response(serializer.data)

    def put(self, request, id=None):
        oldcardata = self.get_object(id)
        newcardata = request.data
        serializer = CarsSerializers(oldcardata, data=newcardata)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        car = self.get_object(id)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# tupe-4
from rest_framework import generics
from rest_framework import mixins


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    
    lookup_field = 'id'
    serializer_class = CarsSerializers
    queryset = Cars.objects.all()
    
    def get(self, request, id=None):
        return self.list(request)
    def post(self, request):
        return self.create(request)

class CarGenerics(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    lookup_field = 'id'
    serializer_class = CarsSerializers
    queryset = Cars.objects.all()

    def get(self, request, id=None):
        return self.retrieve(request, id)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id=None):
        return self.destroy(request, id)

#type-5
from rest_framework import viewsets
from django.shortcuts import get_list_or_404

class CarViewSet(viewsets.ViewSet):
    def list(self, request):
        cars = Cars.objects.all()
        serializer = CarsSerializers(cars, many=True)
        return Response(serializer.data)

    def create(self, request):
        cardata = request.data
        serializer = CarsSerializers(data=cardata)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

