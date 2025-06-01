from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

class ProjectView(APIView):
    def get(self, request):
        link_name = request.query_params.get('link_name')
        if link_name:
            projects = Project.objects.filter(link_name=link_name)
        else:
            projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
