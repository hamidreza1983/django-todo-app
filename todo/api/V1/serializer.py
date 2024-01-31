from rest_framework import serializers
from ...models import *

class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "complete"]
    
    def create(self, validated_data):
        return super().create(validated_data)