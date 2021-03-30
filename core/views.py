from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Pessoa
from django.shortcuts import get_object_or_404  
from django.urls import reverse_lazy


class IndexView(ListView):
    template_name = 'index.html'
    model = Pessoa


class PessoaView(ListView):
    template_name = 'pessoa.html'

    def get_queryset(self):
        self.pessoa = get_object_or_404(Pessoa, id=self.kwargs['pk'])
        if not self.pessoa.mostrar:
            raise Http404

        return self.pessoa


class DeleteViewPessoa(DeleteView):
    model = Pessoa
    success_url = reverse_lazy('index')


class CreatePessoa(CreateView):
    model = Pessoa
    fields = ['nome', 'idade', 'peso', 'genero', 'foto']
    template_name = 'criar_pessoa.html'
    success_url = reverse_lazy('index')


class UpdatePessoa(UpdateView):
    model = Pessoa
    fields = ['nome', 'idade', 'peso', 'genero', 'foto', 'mostrar']
    template_name = 'alterar_pessoa.html'
    success_url = reverse_lazy('index')
    template_name_suffix = '_update_form'

