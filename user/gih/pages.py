# Criados
from ..models import Producto
from ..forms import ProductsForm
# Django
from django.shortcuts import render
from django.urls import reverse_lazy  # redirecionamento em caso de sucessp
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

class IndexView(ListView):
    models = Producto
    template_name = 'index.html'
    queryset = Producto.objects.all()
    context_object_name = 'produtos'

'''

class IndexView(ListView):
    models = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'

class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index') # Quando os produtos forem adicionados com sucesso

class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index') 

class DeleteProdutoView(DeleteView):  # Confirmação de deleção
    model = Produto
    template_name = 'produto_delete.html'
    success_url = reverse_lazy('index')
'''