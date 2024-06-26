from rest_framework import serializers
from .models import Task
from accounts.models import Customer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_customer(self, value):
        if not isinstance(value, Customer):
            raise serializers.ValidationError("Только заказчики могут создавать задачи")
        return value


class TaskAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['executor']

    def update(self, instance, validated_data):
        instance.executor = validated_data.get('executor', instance.executor)
        instance.save()
        return instance