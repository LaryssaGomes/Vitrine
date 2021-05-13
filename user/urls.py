from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView

from .views import IndexView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView, list_products
from django.conf.urls import url

urlpatterns = [
    path('',  list_products, name='shop'),
    path('contas/', include('django.contrib.auth.urls')),
    path('login/', IndexView.as_view(), name='index'), 
    path('<int:pk>/update', UpdateProdutoView.as_view(), name="update"),
    path('<int:pk>/delete', DeleteProdutoView.as_view(), name="delete"),
    path('add/', CreateProdutoView.as_view(), name="add"),
]
