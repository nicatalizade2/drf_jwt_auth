from django.shortcuts import render
from rest_framework.response import Response

from .models import Car
from . serializer import RegisterS, CarSerializer
from rest_framework.views import APIView

class CarList(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

class CarCreate(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class RegistrationAPIView(APIView):
    serializer_class = RegisterS

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)