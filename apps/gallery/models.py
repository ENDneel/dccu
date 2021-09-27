from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=50)
    fecha =models.DateField(auto_now_add=True, verbose_name="Fecha")
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return "%s (ID:%s)" % (self.name, self.id)