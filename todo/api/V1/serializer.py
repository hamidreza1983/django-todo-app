from rest_framework import serializers
from ...models import Task
from accounts.models import CustomeUser





class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields =[
            "id","user", "title" , "complete", 
        ]
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = UserSerializer(instance.user).data
        return rep




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomeUser
        fields = [
            "email" ,"username" 
        ]

