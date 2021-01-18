from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.views.generic import View
from django.http import HttpResponse, HttpResponseServerError, JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class SendMessage(View):

    def get(self, request, *args, **kwargs):
        
        return HttpResponse('This page is not available via http')

    def post(self, request, *args, **kwargs):
        received_json_data = json.loads(request.body.decode("utf-8"))
        name = received_json_data.get('name')
        email = received_json_data.get('email')
        message = received_json_data.get('message')
        composed = f"{message}\n\nfrom {name} - {email}"

        if(message):
            send_mail(
                "Contact message from dianarice.art",
                composed,
                "admin@mail.oh-joy.org",
                ['bradrice1@gmail.com'],
                fail_silently=False
            )
            return HttpResponse('success')

        else:
            HttpResponse('no message sent')

        

        

    # def send_email(self, request):

    #     msg = EmailMessage('Request Callback',
    #         'Here is the message.', to=['bradrice1@gmail.com'])
    #     msg.send()
        

    # def get(self, request, *args, **kwargs):
    #     self.send_email(request)
    #     return HttpResponseRedirect('/')

