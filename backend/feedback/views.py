from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SocialLink
from .serializers import SocialLinkSerializer

@csrf_exempt
def send_feedback(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', 'Guest')
            feedback = data.get('feedback', '')

            if not feedback:
                return JsonResponse({'error': 'Feedback is required'}, status=400)

            subject = f'New Feedback from {username}'
            message = feedback
            recipient_list = ['samuelreegan372@gmail.com']

            send_mail(subject, message, None, recipient_list)

            return JsonResponse({'message': 'Feedback sent successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)



class SocialLinksAPIView(APIView):

    def get(self, request):
        links = SocialLink.objects.all()
        serializer = SocialLinkSerializer(links, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Optional: to update or add social links
        data = request.data
        # data expected as list of dicts [{name:'Instagram', url:'...'}, ...]
        if not isinstance(data, list):
            return Response({"error": "Expected a list of social links."}, status=status.HTTP_400_BAD_REQUEST)

        for link in data:
            obj, created = SocialLink.objects.update_or_create(name=link['name'], defaults={'url': link['url']})
        return Response({"message": "Social links updated"}, status=status.HTTP_200_OK)