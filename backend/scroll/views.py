from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Scroll

class ScrollListAPIView(APIView):
    def get(self, request):
        data = [
            {
                'id': obj.id,
                'scname': obj.scname
            } for obj in Scroll.objects.all()
        ]
        return Response(data)
