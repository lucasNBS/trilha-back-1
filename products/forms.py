from typing import Any
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

  class Meta:
    model = Product
    fields = '__all__'
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-input'}),
      'description': forms.Textarea(attrs={'class': 'form-textarea'}),
      'image': forms.FileInput(attrs={'class': 'form-image'}),
      'price': forms.NumberInput(attrs={'class': 'form-input'}),
      'quantity_in_stock': forms.NumberInput(attrs={'class': 'form-input'}),
      'quantity_sold': forms.NumberInput(attrs={'class': 'form-input'}),
    }

class ProductSellForm(forms.ModelForm):

  class Meta:
    model = Product
    fields = ('quantity_sold', 'quantity_in_stock')
    widgets = {
      'quantity_sold': forms.NumberInput(attrs={'class': 'form-input'}),
      'quantity_in_stock': forms.NumberInput(attrs={'class': 'form-input'}),
    }
  
  def is_valid(self):
    valid = super().is_valid()

    quantity_sold = self.data.get('quantity_sold')
    quantity_in_stock = self.data.get('quantity_in_stock')

    if quantity_in_stock  < 0:
      msg = "There is not enought items in stock"
      self.add_error('quantity_in_stock', msg)
    if quantity_sold < 0:
      msg = "Sales cannot be negative"
      self.add_error('quantity_sold', msg)

    return valid

class ProductStockForm(forms.ModelForm):

  class Meta:
    model = Product
    fields = ('quantity_in_stock',)
    widgets = {
      'quantity_in_stock': forms.NumberInput(attrs={'class': 'form-input'}),
    }

  def clean(self):
    cleaned_data = super().clean()
    
    quantity_in_stock = cleaned_data.get('quantity_in_stock')

    if quantity_in_stock < 0:
      msg = "Stock cannot be negative"
      self.add_error('quantity_in_stock', msg)