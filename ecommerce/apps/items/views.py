from django.shortcuts import render
from rest_framework import viewsets
from .models import Items
from .serializers import ItemSerializer
from rest_framework.permissions import AllowAny
# Create your views here.

# View set

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()

    serializer_class = ItemSerializer

    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.request.query_params.get('userID')

        if user_id:
            return Items.object.filter(user__id = user_id)
        return super().get_queryset()

        
