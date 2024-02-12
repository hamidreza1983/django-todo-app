from rest_framework import serializers
from todo.models import Task

class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "complete"]
    
    def create(self, validated_data):
        return super().create(validated_data)