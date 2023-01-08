from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    # def create(self, validated_data):
    #     car = Car.objects.create(name=validated_data['name'])
    #     car.save()
    #     return car

class RegisterS(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user