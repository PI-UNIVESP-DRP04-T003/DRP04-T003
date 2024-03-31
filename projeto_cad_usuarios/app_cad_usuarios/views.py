from django.shortcuts import render
from .models import usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = usuario()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.rs = request.POST.get("rs")
    novo_usuario.save()

    usuarios = {
        'usuarios': usuario.objects.all()
    }

    return render(request,"usuarios/usuarios.html",usuarios)

    