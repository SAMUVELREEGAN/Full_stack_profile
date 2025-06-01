from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import LandingParaSerializer


class LandingParaList(APIView):
    def get(self, request):
        paras = LandingPara.objects.all()
        serializer = LandingParaSerializer(paras, many=True)
        return Response(serializer.data)


class ThemeSettingsView(APIView):
    def get(self, request):
        themes = ThemeSetting.objects.all()
        return Response({theme.name: theme.colors for theme in themes})