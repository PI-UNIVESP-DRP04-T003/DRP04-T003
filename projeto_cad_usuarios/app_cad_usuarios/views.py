# Inicio Login na página home e link para as páginas pagina1 e pagina 2!

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(requests):
    return render(requests, 'core/home.html')


@login_required
def pagina1(requests):
    return render(requests, 'core/pagina1.html')


@login_required
def pagina2(requests):
    return render(requests, 'core/pagina2.html')

# Inicio parte cadastro !

from django.shortcuts import render
from .models import usuario

def home(request):
    return render(request,'usuarios/cadastro.html')

def usuarios(request):
    novo_usuario = usuario()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.rs = request.POST.get("rs")
    novo_usuario.save()

    usuarios = {
        'usuarios': usuario.objects.all()
    }

    return render(request,"usuarios/usuarios.html",usuarios)

    