from rest_framework import serializers
from .models import Cars

'''
#type - 1
class CarsSerializers(serializers.Serializer):
    car_name = serializers.CharField(max_length=100)
    car_price = serializers.IntegerField()
    fuel_type = serializers.CharField(max_length=100)
    car_feature = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Cars.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.car_name = validated_data.get('car_name', instance.car_name)
        instance.car_price = validated_data.get('car_price', instance.car_price)
        instance.car_namefuel_type = validated_data.get('fuel_type', instance.fuel_type)
        instance.car_feature = validated_data.get('car_feature', instance.car_feature)

        instance.save()
'''

class CarsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = [
            'id',
            'car_name',
            'car_price',
            'fuel_type',
            'car_feature'
        ]