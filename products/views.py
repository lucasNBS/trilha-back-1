from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm

# Create your views here.
class ProductList(ListView):
  model = Product
  paginate_by = 10
  template_name = 'products/products.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    quantity_in_stock = 0
    quantity_sold = 0
    sales_total = 0

    for product in Product.objects.all():
      quantity_in_stock += product.quantity_in_stock
      quantity_sold += product.quantity_sold
      sales_total += product.price * product.quantity_sold

    context['quantity_in_stock'] = quantity_in_stock
    context['quantity_sold'] = quantity_sold
    context['sales_total'] = sales_total

    return context

class ProductDetail(DetailView):
  model = Product
  pk_url_kwarg = 'id'
  template_name = 'products/product.html'

class ProductCreate(CreateView):
  model = Product
  form_class = ProductForm
  template_name = 'products/form.html'
  success_url = reverse_lazy('product-list')

class ProductUpdate(UpdateView):
  model = Product
  form_class = ProductForm
  pk_url_kwarg = 'id'
  template_name = 'products/form.html'
  success_url = reverse_lazy('product-list')

class ProductDelete(DeleteView):
  model = Product
  pk_url_kwarg = 'id'
  template_name = 'pages/confirm_delete.html'
  success_url = reverse_lazy('product-list')