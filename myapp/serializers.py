from rest_framework import serializers
from .models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    projects = serializers.StringRelatedField(many=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'projects']

class ProjectSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True)
    client = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
