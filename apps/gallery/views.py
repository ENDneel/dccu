from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm
from django import forms
from .models import Image
from django.contrib.auth.decorators import login_required

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
    
@login_required(login_url="/login/")
def index(request, template_name='gallery/index.html'):
    images = Image.objects.all()
    for i in images:
        print(i.image)
    data = {
        'object_list': images,
    }
    return render(request, template_name, data)
@login_required(login_url="/login/")
def image_create(request, template_name='gallery/form.html'):
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('gallery:home')
    return render(request, template_name, {'form':form})    
@login_required(login_url="/login/")
def image_update(request, pk, template_name='gallery/form.html'):
    image = get_object_or_404(Image, pk=pk)
    form = ImageForm(request.POST or None, instance=image)
    print("aqui1")
    if form.is_valid():
        form.save()
        print("aqui1 save")
        return redirect('gallery:home')
    return render(request, template_name, {'form':form})
@login_required(login_url="/login/")
def image_delete(request, pk, template_name='gallery/confirm_delete.html'):
    image = get_object_or_404(Image, pk=pk)
    image.delete()
    return redirect('gallery:home') 