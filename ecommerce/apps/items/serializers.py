from rest_framework import serializers
from .models import Items
from apps.users.models import User
from apps.users.enums import UserRoles
# View set
class ItemSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source = 'users.id')


    def create(self, validated_data):
        user = validated_data['user']
        allowed_roles = UserRoles.SHOP

        if user.role not in allowed_roles:
            raise serializers.ValidationError("This action is not allowed")
        return super().create(validated_data)
    
    class Meta:
        model = Items
        fields = '__all__'
        read_only_fields = ['create', 'update', 'price', 'sale_off']
        extra_kwargs = {
            'user': {'required': True}
        }