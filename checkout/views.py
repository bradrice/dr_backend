from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError, JsonResponse 
import stripe
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from dr_backend.settings.base import STRIPEKEY, TWILIOKEY, SMSSENDNUMBER, SMSFROMNUMBER
from twilio.rest import Client
from artwork.models import Artwork



stripe.api_key = STRIPEKEY

@method_decorator(csrf_exempt, name='dispatch')
class CheckoutSession(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('This is GET request')

    def post(self, request, *args, **kwargs):
        received_json_data = json.loads(request.body.decode("utf-8"))
        price = received_json_data.get('price')
        print("price is: ", price)
        price = float(price)
        price = price*100
        price = int(price)
        title = received_json_data.get('title')
        itemid = received_json_data.get('id')

        try:
            intent = stripe.PaymentIntent.create(
                amount=price,
                currency='usd',
                payment_method_types=["card"],
                metadata = {
                    'title': title,
                    'id': itemid
                },
                description="Original artwork (%s) by Diana Rice" % title
            )
            
        except Exception as e:
            print (str(e))
            return HttpResponse(status=403)
        
        return JsonResponse({'clientSecret':intent['client_secret']})


@method_decorator(csrf_exempt, name='dispatch')
class SendSMS(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('This is GET request')

    def post(self, request, *args, **kwargs):
        received_json_data = json.loads(request.body.decode("utf-8"))
        print(received_json_data)
        title = received_json_data.get('title')
        id=received_json_data.get('id')
        art = Artwork.objects.get(id=id)
        art.sold = True;
        art.forSale = False;
        art.save()

        
        # Your Account SID from twilio.com/console
        account_sid = "AC1e8293ab7aa268792f9f6e365ee65ddd"
        # Your Auth Token from twilio.com/console pulled from secret
        auth_token  = TWILIOKEY

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=SMSSENDNUMBER,
            from_=SMSFROMNUMBER,
            body=f"Art - {title} on dianarice.art sold")

        # print(message.sid)


        return JsonResponse({'sid': message.sid, 'status': 'success'})