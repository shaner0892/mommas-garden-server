"""View module for handling requests about users"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mommasgardenapi.models.issue_category import IssueCategory


class IssueCategoryView(ViewSet):
    """Issue Category view"""

    def list(self, request):
        """Handle GET requests to get all issue categories

        Returns:
            Response -- JSON serialized list of all issue categories
        """
        issue_categories = IssueCategory.objects.all()
        serializer = IssueCategorySerializer(issue_categories, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Handle GET requests for a single issue category

        Returns:
            Response -- JSON serialized issue category
        """
        issue_category = IssueCategory.objects.get(pk=pk)
        serializer = IssueCategorySerializer(issue_category)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized issue category instance
        """
        serializer = CreateIssueCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for an issue category

        Returns:
            Response -- Empty body with 204 status code
        """

        issue_category = IssueCategory.objects.get(pk=pk)
        issue_category.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk):
        """Handle DELETE requests for an issue category
        """
        issue_category = IssueCategory.objects.get(pk=pk)
        issue_category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class IssueCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueCategory
        fields = ('id', 'type')
        
class CreateIssueCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueCategory
        fields = ['id', 'type']
