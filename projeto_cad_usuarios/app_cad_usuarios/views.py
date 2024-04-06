<<<<<<< HEAD
from django.shortcuts import render, redirect, reverse
from .models import Houses
from django.views.generic import View
import pandas as pd
import plotly.express as px
import plotly.offline as py
from plotly.offline import plot
import plotly.graph_objs as go

class HousesView(View):
    def get(self, request, *args, **kwargs):
        data = Houses.objects.all()
        houses_df = [
            {
                'yr_built': x.yr_built,
                'price': x.price
            } for x in data
            ]

        df = pd.DataFrame(houses_df)

        fig1 = px.scatter(df, x='yr_built', y='price')

        fig_plot = plot(fig1, output_type = 'div')

        ctx = {'fig1': fig_plot}
        return render(request, 'usuarios/home.html', ctx)
=======
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

    
>>>>>>> front
