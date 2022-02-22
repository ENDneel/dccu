from rest_framework import viewsets
from .models import Image
from .serializer import ImageSerializer

# tipo de Vista basada en clase, que no proporciona metodos como listar y crear
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
