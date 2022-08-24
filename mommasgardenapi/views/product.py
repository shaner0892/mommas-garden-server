"""View module for handling requests about users"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mommasgardenapi.models.plant import Plant
from mommasgardenapi.models.product import Product


class ProductView(ViewSet):
    """Product view"""

    def list(self, request):
        """Handle GET requests to get all products

        Returns:
            Response -- JSON serialized list of all products
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Handle GET requests for a single product

        Returns:
            Response -- JSON serialized product
        """
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized product instance
        """
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a product

        Returns:
            Response -- Empty body with 204 status code
        """

        product = Product.objects.get(pk=pk)
        plant = Plant.objects.get(pk=request.data["plant"])
        product.plant = plant
        product.harvest_date = request.data["harvest_date"]
        product.url = request.data["url"]
        product.note = request.data["note"]
        product.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk):
        """Handle DELETE requests for a product
        """
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'plant', 'harvest_date', 'url', 'note')
        depth = 2
        
class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'plant', 'harvest_date', 'url', 'note']
