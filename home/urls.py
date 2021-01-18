from django.urls import path
from . import views

urlpatterns = [
    path('api/homepage/', views.HomePageDetail.as_view()),
]