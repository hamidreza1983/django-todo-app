from rest_framework import serializers
from ...models import Task


class TaskSerializer(serializers.ModelSerializer):
   
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        kwargs = request.parser_context.get('kwargs')
        if kwargs.get('pk') is not None:
            rep.pop('content')
        return rep
    
    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        
        return super().create(validated_data)    
    
    class Meta:
        model = Task
        fields = ["id", "title"]