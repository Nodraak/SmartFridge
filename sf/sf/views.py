#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from .models import Product
from .forms import FindForm

# home
def index(request):
    return render(request, 'sf/index.html')

# trouver si produit est ds le frigo
def find_product(request):

    if request.method == 'GET':
        c = {
            'form': FindForm(),
        }
        return render(request, 'sf/find_product.html', c)
    else:  # POST
        form = FindForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']


            return redirect('sf:find_product')
        else:  # ie. not valid
            c = {
                'form': form,
            }
            return render(request, 'sf/find_product.html', c)

    return render(request, 'sf/find_product.html')

# sortir un produit + liaison serie
def get(request):
    return render(request, 'sf/get.html')

# entrer un nouveau produit -> trouver une place
def new(request):
    return render(request, 'sf/new.html')

# trouver recette
def find_recipe(request):
    return render(request, 'sf/find_recipe.html')

# montrer la liste
def show_list(request):
    p = Product.objects.all()

    c = {
        'products': p,
    }

    return render(request, 'sf/show_list.html', c)

# trouver les produits associés a la recette
# TODO


from django import forms
from .models import ArduiSerial

class DebugForm(forms.Form):
    order = forms.CharField()

# montrer la liste
def debug(request):
    if request.method == 'POST':
        form = DebugForm(request.POST)
        if form.is_valid():
            order = int(form.cleaned_data['order'], 2)

            a = ArduiSerial(port='/dev/ttyACM1')

            ret = a._order_send(order)

            return render(request, 'sf/debug.html', {'ret': ret})
    else:  # method == GET
        form = DebugForm(initial={'order': '10000001'})
    return render(request, 'sf/debug.html', {'form': form})
