from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import MyContactSerializer

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives
import json


class MyContactView(APIView):
    def get(self, request):
        contact = MyContact.objects.first()
        serializer = MyContactSerializer(contact)
        return Response(serializer.data)

@csrf_exempt
def contact_form_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON'}, status=400)

        form_type = data.get('type')
        user_email = data.get('email')

        if not form_type:
            return JsonResponse({'success': False, 'message': 'Form type is missing'}, status=400)
        if not user_email:
            return JsonResponse({'success': False, 'message': 'User email is missing'}, status=400)

        # Admin Email HTML
        admin_html_message = "<h2>New Contact Form Submission</h2><ul>"
        for key, value in data.items():
            admin_html_message += f"<li><strong>{key}:</strong> {value}</li>"
        admin_html_message += "</ul>"

        admin_email = EmailMultiAlternatives(
            subject=f"New Contact Form Submission: {form_type}",
            body="You have a new contact form submission.",
            from_email='samuelreegan372@gmail.com',
            to=['samuelreegan372@gmail.com'],
        )
        admin_email.attach_alternative(admin_html_message, "text/html")
        admin_email.send()

        # Fetch user message
        try:
            auto_reply_obj = AutoReplyMessage.objects.get(form_type=form_type)
            user_message = auto_reply_obj.message
        except AutoReplyMessage.DoesNotExist:
            user_message = "Thank you for contacting us!"

        # ✅ Beautiful User Email HTML
        user_html_message = f"""
        <html>
        <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 30px;">
          <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <h2 style="color: #00796b;">Thank You for Reaching Out!</h2>
            <p style="font-size: 16px; color: #333333;">{user_message.replace('\n', '<br>')}</p>
            <hr style="margin: 20px 0;">
            <p style="font-size: 14px; color: #888888;">We appreciate your interest. You will hear from us soon!</p>
            <p style="font-size: 14px; color: #888888;">Best regards,<br><strong>Samuvel Reegan</strong></p>
          </div>
        </body>
        </html>
        """

        user_email_msg = EmailMultiAlternatives(
            subject="Thank You for Contacting Us",
            body=user_message,
            from_email='samuelreegan372@gmail.com',
            to=[user_email],
        )
        user_email_msg.attach_alternative(user_html_message, "text/html")
        user_email_msg.send()

        return JsonResponse({'success': True, 'message': 'Form submitted and emails sent.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)
