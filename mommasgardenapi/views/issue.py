"""View module for handling requests about users"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mommasgardenapi.models.issue import Issue
from mommasgardenapi.models.issue_category import IssueCategory
from mommasgardenapi.models.plant import Plant


class IssueView(ViewSet):
    """Issue view"""

    def list(self, request):
        """Handle GET requests to get all issues

        Returns:
            Response -- JSON serialized list of all issues
        """
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Handle GET requests for a single issue

        Returns:
            Response -- JSON serialized issue
        """
        issue = Issue.objects.get(pk=pk)
        serializer = IssueSerializer(issue)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized issue instance
        """
        serializer = CreateIssueSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for an issue

        Returns:
            Response -- Empty body with 204 status code
        """

        issue = Issue.objects.get(pk=pk)
        plant = Plant.objects.get(pk=request.data["plant"])
        category = IssueCategory.objects.get(pk=request.data["category"])
        issue.plant = plant
        issue.category = category
        issue.note = request.data["note"]
        issue.date = request.data["date"]
        issue.url = request.data["url"]
        issue.solution = request.data["solution"]
        issue.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk):
        """Handle DELETE requests for an issue
        """
        issue = Issue.objects.get(pk=pk)
        issue.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'category', 'note', 'date', 'plant', 'url', 'solution')
        depth = 2
        
class CreateIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'category', 'note', 'date', 'plant', 'url', 'solution']
