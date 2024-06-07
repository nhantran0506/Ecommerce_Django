from django.shortcuts import render
from .models import User
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            password = serializer.validated_data.get('password')
            if password:
                user.set_password(password)
                user.save()
            return Response({"message" :"User created successfully!"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data

        allow_updates = ['name', 'date_of_birth']
        for field in list(data.keys()):
            if field not in allow_updates:
                data.pop(field)
        
        serializer = self.get_serializer(instance, data=data,partial= partial)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User updated successfully!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
