from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question

class QuestionListAPIView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        data = [
            {
                'id': q.id,
                'qus': q.qus,
                'ans': q.ans
            }
            for q in questions
        ]
        return Response(data)
