"""View module for handling requests about users"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mommasgardenapi.models.gardener import Gardener


class GardenerView(ViewSet):
    """Gardener view"""

    def list(self, request):
        """Handle GET requests to get all users

        Returns:
            Response -- JSON serialized list of all users
        """
        gardeners = Gardener.objects.all()
        serializer = GardenerSerializer(gardeners, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Handle GET requests for single user

        Returns:
            Response -- JSON serialized user
        """
        gardener = Gardener.objects.get(user=request.auth.user)
        serializer = GardenerSerializer(gardener)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a user

        Returns:
            Response -- Empty body with 204 status code
        """

        gardener = Gardener.objects.get(pk=pk)
        user = User.objects.get(pk=gardener.user_id)
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.username = request.data["username"]
        user.email = request.data["email"]
        user.is_active = request.data["is_active"]
        user.save()
        gardener.bio = request.data["bio"]
        gardener.url = request.data["url"]
        gardener.location = request.data["location"]
        gardener.planting_zone = request.data["planting_zone"]
        gardener.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff')


class GardenerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Gardener
        fields = ('id', 'bio', 'location', 'url', 'planting_zone', 'user')
        depth = 2