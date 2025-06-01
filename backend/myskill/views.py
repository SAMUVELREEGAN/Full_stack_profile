from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Myskill

class MyskillListAPIView(APIView):
    def get(self, request):
        skills = Myskill.objects.all()
        data = [
            {
                'id': skill.id,
                'pic': request.build_absolute_uri(skill.pic.url) if skill.pic else '',
                'name': skill.name,
                'percentage': skill.percentage,
                'rangecolor': skill.rangecolor,
            } for skill in skills
        ]
        return Response(data)
