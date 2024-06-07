from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'name', 'password', 'date_of_birth']
        extra_kwargs ={
            "password" : {'write_only' : True , 'required' : False},
            "date_of_birth" : {'write_only' : True , 'required' : False},
        }

        def update(self, instance, valid_data):
            valid_data.pop('password', None)
            instance = super.update(instance, valid_data)
            return instance
    
