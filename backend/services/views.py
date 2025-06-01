from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service

class ServiceListAPIView(APIView):
    def get(self, request):
        data = [
            {
                'id': service.id,
                'pic': request.build_absolute_uri(service.pic.url) if service.pic else '',
                'title': service.title,
                'contant': service.contant
            } for service in Service.objects.all()
        ]
        return Response(data)
