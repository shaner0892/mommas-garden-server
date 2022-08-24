"""View module for handling requests about users"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mommasgardenapi.models.plant_type import PlantType


class PlantTypeView(ViewSet):
    """Plant type view"""

    def list(self, request):
        """Handle GET requests to get all plant types

        Returns:
            Response -- JSON serialized list of all plant types
        """
        plant_types = PlantType.objects.all()
        serializer = PlantTypeSerializer(plant_types, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Handle GET requests for a single plant type

        Returns:
            Response -- JSON serialized plant type
        """
        plant_type = PlantType.objects.get(pk=pk)
        serializer = PlantTypeSerializer(plant_type)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized plant type instance
        """
        serializer = CreatePlantTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a plant type

        Returns:
            Response -- Empty body with 204 status code
        """

        plant_type = PlantType.objects.get(pk=pk)
        plant_type.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk):
        """Handle DELETE requests for a plant type
        """
        plant_type = PlantType.objects.get(pk=pk)
        plant_type.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class PlantTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantType
        fields = ('id', 'type')
        
class CreatePlantTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantType
        fields = ['id', 'type']
