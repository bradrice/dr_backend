from django.urls import path
from . import views

urlpatterns = [
    path('create-payment-intent', views.CheckoutSession.as_view(), name='create-intent'),
    path('send-sms-success', views.SendSMS.as_view(), name='csend-sms'),

    # path('checkout/', views.CheckoutSession.as_view(), name="checkout-session"),
    ]