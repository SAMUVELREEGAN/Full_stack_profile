from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Detail
from .serializers import DetailSerializer

class DetailView(APIView):
    def get(self, request):
        detail = Detail.objects.first()
        serializer = DetailSerializer(detail)
        return Response(serializer.data)
