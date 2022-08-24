"""View module for handling requests about users"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mommasgardenapi.models.gardener import Gardener
from mommasgardenapi.models.plant import Plant
from mommasgardenapi.models.plant_type import PlantType


class PlantView(ViewSet):
    """Plant view"""

    def list(self, request):
        """Handle GET requests to get all plants

        Returns:
            Response -- JSON serialized list of all plants
        """
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Handle GET requests for a single plant

        Returns:
            Response -- JSON serialized plant
        """
        plant = Plant.objects.get(pk=pk)
        serializer = PlantSerializer(plant)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized plant instance
        """
        gardener = Gardener.objects.get(user=request.auth.user)
        serializer = CreatePlantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gardener=gardener)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a plant

        Returns:
            Response -- Empty body with 204 status code
        """

        plant = Plant.objects.get(pk=pk)
        type = PlantType.objects.get(pk=request.data["type"])
        plant.type = type
        plant.species = request.data["species"]
        plant.date_planted = request.data["date_planted"]
        plant.producing = request.data["producing"]
        plant.url = request.data["url"]
        plant.perennial = request.data["perennial"]
        plant.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk):
        """Handle DELETE requests for a plant
        """
        plant = Plant.objects.get(pk=pk)
        plant.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'species', 'date_planted', 'producing', 'type', 'url', 'perennial', 'gardener')
        depth = 2
        
class CreatePlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'species', 'date_planted', 'producing', 'type', 'url', 'perennial', 'gardener']
