from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Experience
from .serializers import ExperienceSerializer

class ExperienceView(APIView):
    def get(self, request):
        experiences = Experience.objects.all().order_by('id')
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data)
