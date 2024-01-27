from rest_framework import serializers
from ...models import Task






class TaskSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)    

    class Meta:
        model = Task
        fields =[
            "title" , "complete", 
        ]
    
   

