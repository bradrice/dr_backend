from django.urls import path, re_path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api/artwork/', views.ArtworkListCreate.as_view() ),
    path('api/allartwork/', views.ArtworkFullListCreate.as_view() ),
    path('api/artwork/<int:pk>', views.ArtworkDetail.as_view(), name="detail" ),
    path('api/artwork/media/', views.ArtworkMediaList.as_view(), name="media-list"),
    path('api/artwork/isSold/<int:pk>', views.ArworkIsSold.as_view(), name='is_sold'),
    path('api/artwork/mediatypes', views.ArtworkMediaTypes.as_view(), name='media-types')
]