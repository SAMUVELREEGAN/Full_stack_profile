from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Visitor
from .serializers import VisitorSerializer

class VisitorCreateAPIView(APIView):
    def post(self, request):
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Visitor saved!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        visitors = Visitor.objects.all().order_by('-visited_at')  # Optional ordering
        serializer = VisitorSerializer(visitors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
