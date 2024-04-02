from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product

# Create your views here.
class ProductList(ListView):
  model = Product
  template_name = 'products/products.html'

class ProductDetail(DetailView):
  model = Product
  pk_url_kwarg = 'id'

class ProductCreate(CreateView):
  model = Product

class ProductUpdate(UpdateView):
  model = Product
  pk_url_kwarg = 'id'

class ProductDelete(DeleteView):
  model = Product
  pk_url_kwarg = 'id'