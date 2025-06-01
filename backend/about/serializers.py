from rest_framework import serializers
from .models import About, AboutList

class AboutListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutList
        fields = ['count', 'type1']

class AboutSerializer(serializers.ModelSerializer):
    lists = AboutListSerializer(many=True, read_only=True)
    pic = serializers.ImageField(use_url=True)

    class Meta:
        model = About
        fields = ['id', 'question', 'name', 'pic', 'contant', 'lists']
