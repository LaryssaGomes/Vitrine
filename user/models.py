from django.db import models
from django.contrib.auth.models import AbstractUser
from stdimage.models import StdImageField
# Create your models here.
class Usuario(AbstractUser): 
    ...

class Producto(models.Model):
    PRODUCTS_CHOICE = (
        ("Calca", "Calça"),
        ("Camisa", "Camisa"),
        ("Bermuda", "Bermuda"),
        ("Saia", "Saia"),  
        ("Vestido", "Vestido"),      
    )  
    pro_inst = models.CharField('Tipo:', max_length=9, choices=PRODUCTS_CHOICE)
    pro_name = models.CharField('Nome',max_length=255)
    pro_description = models.TextField('Descrição',max_length=255)
    pro_price = models.DecimalField('Preço',max_digits=6, decimal_places=2)
    pro_img = StdImageField('Foto', upload_to='Producto')