from .models import Image
from rest_framework import serializers

# Imagen serializable Los serializadores permiten convertir 
# datos complejos, como conjuntos de consultas e instancias de 
# modelos, en tipos de datos nativos de Python
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields = '__all__'
        