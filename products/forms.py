from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

  class Meta:
    model = Product
    fields = '__all__'
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-input'}),
      'description': forms.Textarea(attrs={'class': 'form-textarea'}),
      'image': forms.FileField(attrs={'class': 'form-image'}),
      'price': forms.NumberInput(attrs={'class': 'form-input'}),
      'quantity_in_stock': forms.NumberInput(attrs={'class': 'form-input'}),
      'quantity_sold': forms.NumberInput(attrs={'class': 'form-input'}),
    }