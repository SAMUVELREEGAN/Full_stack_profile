from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProjectURl
from .serializers import ProjectSerializer

class ProjectList(APIView):
    def get(self, request):
        projects = ProjectURl.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
