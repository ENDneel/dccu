from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm
from django import forms
from .models import Image
from django.contrib.auth.decorators import login_required
import os

## clase ModelForm nos permite tener el manejo y control de los formularios 
class ImageForm(ModelForm):
    name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "name",
                    "placeholder": "Ingrese nombre de paciente",
                    "data-sb-validations":"required",
                    "onkeyup":"replaceName(this)"
                }
            ))

    image = forms.ImageField(required=False,  widget=forms.FileInput(attrs={
         "class":"btn btn-xl",
         "type":"file",
    }))
    

    class Meta:
        model = Image
        fields = ['name', 'image']
## Metodo index, es llamado al iniciar la pagina principal
@login_required(login_url="/login/")
def index(request, template_name='gallery/index.html'):
    #Traer todas la imagenes
    images = Image.objects.all()
    data = {
        'object_list': images,
    }
    return render(request, template_name, data)
    #Metodo para subir una imagen al servidor 
@login_required(login_url="/login/")
def image_create(request, template_name='gallery/form.html'):
    #verificamos si el formulario es el correcto 
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        #guardamos el formulario
        form.save()
        return redirect('gallery:home')
    return render(request, template_name, {'form':form})    

    ##Metodo para Actualizar la imagen 
@login_required(login_url="/login/")
def image_update(request, pk, template_name='gallery/form.html'):
    ##Buscamos la imagen en el caso de existir 
    image = get_object_or_404(Image, pk=pk)
    #Verificamos si los datos son correctos
    form = ImageForm(request.POST or None, instance=image)
    if form.is_valid():
        form.save()
        return redirect('gallery:home')
    return render(request, template_name, {'form':form})
    ##Metodo para eliminar la imagen 
@login_required(login_url="/login/")
def image_delete(request, pk, template_name='gallery/confirm_delete.html'):
    ##Buscamos la imagen y si existe se procede a borrar
    image = get_object_or_404(Image, pk=pk)
    image.delete()
    return redirect('gallery:home') 

##Metodo para descargar la aplicacion movil
def descargarApk(request):
    #ruta de donde se encuentra el archivo 
    file_path = "dccuV1.apk"
    #verificamos si existe
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            #genramos un response el cual el cual contiene la aplicacion 
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            #usamos Content-Disposition el cual indica si el contenido se espera que se muestre en línea en el navegador, esto es, 
            #como una o como parte de una página web, o como un archivo adjunto, que se puede descargar y 
            #guardar localmente
            response["Content-Disposition"] = "inline; filename=" + os.path.basename(
                file_path
            )
            return response
    return render(request, "404.html")