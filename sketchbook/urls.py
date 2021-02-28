from django.urls import path, re_path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api/sketchbook/', views.SketchbookListCreate.as_view() ),
    path('api/allsketchbook/', views.SketchbookFullListCreate.as_view() ),
    path('api/sketchbook/<int:pk>', views.SketchbookDetail.as_view(), name="detail" ),
    path('api/sketchbook/media/', views.SketchbookMediaList.as_view(), name="media-list"),
    path('api/sketchbook/mediatypes', views.SketchbookMediaTypes.as_view(), name='media-types')
]