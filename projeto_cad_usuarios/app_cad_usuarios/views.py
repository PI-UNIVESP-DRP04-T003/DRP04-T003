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