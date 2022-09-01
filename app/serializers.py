from rest_framework import serializers
from .models import Position, Employee


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    birth_year = serializers.IntegerField()
    position = serializers.CharField(max_length=100)
    salary = serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.birth_year = validated_data.get('birth_year')
        instance.position = validated_data.get('position')
        instance.salary = validated_data.get('salary')
        instance.save()
        return instance
