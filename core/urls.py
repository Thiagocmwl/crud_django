from django.urls import path
from .views import IndexView, PessoaView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pessoa/<int:pk>', PessoaView.as_view(), name='pessoa')
]