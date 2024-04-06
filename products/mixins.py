from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import BaseUpdateView

class ProductModalMixin(BaseUpdateView):
  pk_url_kwarg = 'id'
  type = None

  def get(self, request, *args, **kwargs):
    context = {
      'product': self.get_object(),
      'form': self.get_form(),
      'errors': self.get_form().errors,
      'type': self.type,
    }

    return render(request, 'products/modal.html', context)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['errors'] = self.get_form().errors
    context['type'] = self.type

  def form_valid(self, form):
    form.save()
    return HttpResponse('<script>window.parent.document.querySelector("#modal-frame").src = "";window.parent.document.querySelector("#background").classList.add("disapear");window.parent.window.location.reload();</script>')
  
  def form_invalid(self, form):
    
    context = {
      'product': self.get_object(),
      'errors': form.errors,
      'form': self.form_class,
      'type': self.type,
    }

    return render(self.request, 'products/modal.html', context)
