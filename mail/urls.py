from django.urls import path
from . import views

urlpatterns = [
    path('message', views.SendMessage.as_view(), name='contact-message'),
    # path('checkout/', views.CheckoutSession.as_view(), name="checkout-session"),
    ]