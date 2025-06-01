from rest_framework import serializers
from .models import EducationGroup, EducationItem

class EducationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationItem
        fields = ['passedout', 'institute', 'locations', 'sub']

class EducationGroupSerializer(serializers.ModelSerializer):
    one = EducationItemSerializer(many=True, read_only=True)

    class Meta:
        model = EducationGroup
        fields = ['id', 'heading', 'one']
