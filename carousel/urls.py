from django.urls import path
from . import views

urlpatterns = [
    path('api/carousel/', views.CarouselListCreate.as_view()),
    path('api/carousel/<int:pk>', views.CarouselDetail.as_view(), name="carouseldetail" ),
]