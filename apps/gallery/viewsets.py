from rest_framework import viewsets
from .models import Image
from .serializer import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
