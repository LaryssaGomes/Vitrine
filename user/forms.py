from .models import Usuario, Producto
from django import forms

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('pro_inst',
                  'pro_name',
                  'pro_description',
                  'pro_price',
                  'pro_img')
        