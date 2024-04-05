from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm, ProductSellForm, ProductStockForm

def overview_data(context):
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

# Create your views here.
class ProductList(ListView):
  model = Product
  paginate_by = 5
  template_name = 'products/products.html'

  def get_queryset(self):
    queryset = super().get_queryset()

    price_min = self.request.GET.get('price-min')
    price_max = self.request.GET.get('price-max')

    if price_min == '' or price_min == None:
      price_min = 0
    else:
      queryset = queryset.filter(price__gte=price_min)

    if price_max != '' and price_max != None:
      queryset = queryset.filter(price__lte=price_max)

    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    price_min = self.request.GET.get('price-min')
    price_max = self.request.GET.get('price-max')

    if price_min == None:
      price_min = ''
    if price_max == None:
      price_max = ''

    context['price_min'] = price_min
    context['price_max'] = price_max

    overview_data(context)

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

def ProductSell(request, id):
  product = get_object_or_404(Product, id=id)
  product_quantity_sold = product.quantity_sold
  product_quantity_stock = product.quantity_in_stock

  form = ProductSellForm()
  errors = form.errors

  action_type = request.POST.get('action-type')
  quantity = request.POST.get('quantity_sold')

  if request.method == 'POST':
    post = request.POST.copy()

    if action_type == 'Add':
      post.update({'quantity_sold': product_quantity_sold + float(quantity)})
      post.update({'quantity_in_stock': product_quantity_stock - float(quantity)})
    if action_type == 'Remove':
      post.update({'quantity_sold': product_quantity_sold - float(quantity)})
      post.update({'quantity_in_stock': product_quantity_stock + float(quantity)})

    request.POST = post
    form = ProductSellForm(request.POST, instance=product)
    errors = form.errors
    if form.is_valid():
      form.save()
      form = ProductSellForm(instance=product)
      return HttpResponse('<script>window.parent.document.querySelector("#modal-frame").src = "";window.parent.document.querySelector("#background").classList.add("disapear");window.parent.window.location.reload();</script>')
    else:
      form = ProductSellForm()
    
  context = {
    'product': product,
    'form': form,
    'errors': errors,
    'type': 'Sell',
  }

  overview_data(context)

  return render(request, 'products/modal.html', context)

def ProductStock(request, id):
  product = get_object_or_404(Product, id=id)
  product_quantity_stock = product.quantity_in_stock

  form = ProductStockForm()
  errors = form.errors

  action_type = request.POST.get('action-type')
  quantity = request.POST.get('quantity_in_stock')

  if request.method == 'POST':
    post = request.POST.copy()

    if action_type == 'Add':
      post.update({'quantity_in_stock': product_quantity_stock + float(quantity)})
    if action_type == 'Remove':
      post.update({'quantity_in_stock': product_quantity_stock - float(quantity)})

    request.POST = post
    form = ProductStockForm(request.POST, instance=product)
    errors = form.errors
    if form.is_valid():
      form.save()
      form = ProductStockForm(instance=product)
      return HttpResponse('<script>window.parent.document.querySelector("#modal-frame").src = "";window.parent.document.querySelector("#background").classList.add("disapear");window.parent.window.location.reload();</script>')
    else:
      form = ProductStockForm()

  context = {
    'product': product,
    'form': form,
    'errors': errors,
    'type': 'Stock',
  }

  overview_data(context)

  return render(request, 'products/modal.html', context)