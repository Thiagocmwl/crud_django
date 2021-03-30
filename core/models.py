from django.db import models
from uuid import uuid4


def get_auto_path(_instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid4()}.{ext}'
    return new_filename


class Base(models.Model):
    criacao = models.DateTimeField('Criação', auto_now_add=True)
    alteracao = models.DateTimeField('Alteração', auto_now=True)

    class Meta:
        abstract = True


class Pessoa(Base):
    GENERO_CHOICES = (
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro')
    )

    nome = models.CharField('Nome', max_length=100)
    idade = models.IntegerField('Idade')
    peso = models.DecimalField('Peso', decimal_places=2, max_digits=5)
    genero = models.CharField('Gênero', max_length=len('Masculino'), choices=GENERO_CHOICES)
    foto = models.ImageField('Foto', upload_to=get_auto_path)
    mostrar = models.BooleanField('Mostrar?', default=True)
