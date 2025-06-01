from rest_framework.views import APIView
from rest_framework.response import Response
from .models import About
from .serializers import AboutSerializer

class AboutView(APIView):
    def get(self, request):
        about_data = About.objects.all()
        serializer = AboutSerializer(about_data, many=True, context={"request": request})
        return Response(serializer.data)
