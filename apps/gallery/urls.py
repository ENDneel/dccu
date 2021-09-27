from django.urls import path

from . import views
from rest_framework import routers
from .viewsets import ImageViewSet

app_name = 'gallery'

router = routers.SimpleRouter()
router.register(r'restgallery', ImageViewSet)

urlpatterns = [
  path('', views.index, name='home'),
  path('new/', views.image_create, name='image_new'),
  path('edit/<int:pk>/', views.image_update, name='image_edit'),
  path('delete/<int:pk>/', views.image_delete, name='image_delete'),
]
urlpatterns += router.urls