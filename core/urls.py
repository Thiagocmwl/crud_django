from django.urls import path
from .views import IndexView, PessoaView, DeleteViewPessoa, CreatePessoa, UpdatePessoa


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pessoa/<int:pk>', PessoaView.as_view(), name='pessoa'),
    path('<int:pk>', DeleteViewPessoa.as_view(), name='delete'),
    path('pessoa/criar', CreatePessoa.as_view(), name='create'),
    path('update/<int:pk>', UpdatePessoa.as_view(), name='update')
]