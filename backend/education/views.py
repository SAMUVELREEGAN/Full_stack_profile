from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EducationGroup
from .serializers import EducationGroupSerializer

class EducationGroupView(APIView):
    def get(self, request):
        groups = EducationGroup.objects.all()
        serializer = EducationGroupSerializer(groups, many=True)
        return Response(serializer.data)
