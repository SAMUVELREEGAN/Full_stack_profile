from rest_framework import serializers
from .models import ProjectURl

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectURl
        fields = ['pro_name', 'pro_url']
