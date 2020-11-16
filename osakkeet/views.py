import pandas
import matplotlib.pyplot as plt

from django.shortcuts import render
from django.views import generic, View
from django.db.models import Avg, Count, Min, Sum

from .models import Osakkeet
from .forms import OsakkeetForm

# Create your views here.


class OsakeLista(generic.ListView):
    model = Osakkeet

    def arvo(self):
        return Osakkeet.objects.aggregate(Sum('arvo'))

    def osinko(self):
        return Osakkeet.objects.aggregate(Sum('osingot'))

    def ekselkamaa(self):
        """ df.to_html osakkeet_list -templatelle {{ views.ekselkamaa.df.to_html|safe }}.  That's all. Siistii!!"""
        df = pandas.read_csv('osakkeet/kia_osakkeet.csv', index_col='Osake')

        totalarvo = df['Arvo'].sum()
        totalosingot = df['Osingot'].sum()
        context = {
            'df': df,
            'totalarvo': totalarvo,
            'totalosingot': totalosingot,
        }
        return context


def new(request):
    if request.method == 'POST':
        form = OsakkeetForm(request.POST)
        if form.is_valid():
            osake = Osakkeet(
            nimi=form.cleaned_data["nimi"],
            maara=form.cleaned_data['maara'],
            osingot=form.cleaned_data['osingot']
            )
            osake.save()
            return render(request, 'osakkeet/osakkeet_list.html')
    else:
        form = OsakkeetForm()

    return render(request, 'osakkeet/osake_edit.html', {'form': form})
