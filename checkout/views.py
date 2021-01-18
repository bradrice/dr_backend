from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError, JsonResponse 
import stripe
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from bb_backend.settings.base import STRIPEKEY

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
                description="Original artwork (%s) by Brad Rice" % title
            )
            
        except Exception as e:
            print (str(e))
            return HttpResponse(status=403)
                # return jsonify(error=str(e)), 403
        # session = stripe.checkout.Session.create(
        #     payment_method_types=['card'],
        #     line_items=[{
        #     'price_data': {
        #         'currency': 'usd',
        #         'product_data': {
        #         'name': 'Artwork',
        #         },
        #         'unit_amount': price,
        #     },
        #     'quantity': 1,
        #     }],
        #     mode='payment',
        #     description= title,
            
        #     success_url='http://localhost:3000/checkout/success',
        #     cancel_url='http://localhost:3000/checkout/cancel',
        # )
        # return HttpResponse(session.id, content_type='application/json')
        return JsonResponse({'clientSecret':intent['client_secret']})

