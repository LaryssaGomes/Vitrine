# Django
from django.shortcuts import render,redirect 
from django.urls import reverse_lazy  # redirecionamento em caso de sucessp
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.paginator import Paginator
from .forms import ProductsForm
from .models import Producto
from django.contrib.auth.decorators import login_required


def list_products(request):
    name = request.POST.get('search')
    if name != None:
        producto = Producto.objects.filter(pro_name__icontains = name).exists()
        
        if producto is True:
            producto = Producto.objects.filter(pro_name__icontains = name)
            return render(request, 'user/shop.html', {'produtos':producto})
    
    producto = Producto.objects.all()
    return render(request, 'user/shop.html', {'produtos':producto})


class IndexView(ListView):
    models = Producto
    template_name = 'index.html'
    queryset = Producto.objects.all()
    context_object_name = 'produtos'
    paginate_by = 3


class CreateProdutoView(CreateView):
    login_required = True
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('index') 

class UpdateProdutoView(UpdateView):
    login_required = True
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('index') 

class DeleteProdutoView(DeleteView):  # Confirmação de deleção
    login_required = True
    model = Producto
    success_url = reverse_lazy('index')

