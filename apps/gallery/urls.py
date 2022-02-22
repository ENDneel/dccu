from django.urls import path

from . import views
from rest_framework import routers
from .viewsets import ImageViewSet
#nombre de entorno en el que se trabaja
app_name = 'gallery'
# funcionalidad para determinar automáticamente
# cómo se deben asignar las URL de una aplicación a la lógica 
# que se ocupa del manejo de las solicitudes entrantes.
router = routers.SimpleRouter()
#url para el consumo de las imagenes
router.register(r'restgallery', ImageViewSet)
#urls 
urlpatterns = [
  path('', views.index, name='home'),
  path('new/', views.image_create, name='image_new'),
  path('edit/<int:pk>/', views.image_update, name='image_edit'),
  path('delete/<int:pk>/', views.image_delete, name='image_delete'),
  path('descarga/apk/', views.descargarApk, name="descarga_apk"),
]
urlpatterns += router.urls