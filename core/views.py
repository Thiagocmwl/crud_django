from django.shortcuts import render
from django.views.generic import ListView
from .models import Pessoa
from django.shortcuts import get_object_or_404  


class IndexView(ListView):
    template_name = 'index.html'
    model = Pessoa


class PessoaView(ListView):
    template_name = 'pessoa.html'

    def get_queryset(self):
        self.pessoa = get_object_or_404(Pessoa, id=self.kwargs['pk'])

        return self.pessoa


