from typing import Any
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseNotFound
from .models import GuilhermeModel
from .forms import GuilhermeForm
from django.views import generic

def create_view(request):
    context = {}
    form = GuilhermeForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('crud:listar')
    context['form'] = form
    return render(request, "create_view.html", context)

class ListView(generic.ListView):
    model = GuilhermeModel

    # def get_context_data(self, **kwargs):
    #     context = super(ListView,self).get_context_data(**kwargs)
    #     teste = [e.id for e in context['object_list']]
    #     context['id'] = teste
    #     return context

    

class DetailView(generic.DetailView):
    model = GuilhermeModel

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset=queryset)
        except:
            return None

class DeleteView(generic.DeleteView):
    model = GuilhermeModel
    success_url = '/crud/list'
