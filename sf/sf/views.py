#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from .models import Product, Position
from .forms import NewForm, FindForm

from .models import Product

# home
def index(request):
    return render(request, 'sf/index.html')


# entrer un nouveau produit -> trouver une place
def new(request):

    if request.method == 'GET':
        c = {
            'form': NewForm(),
        }
        return render(request, 'sf/new.html', c)
    else:  # POST
        form = NewForm(request.POST)
        if form.is_valid():
            p = Product()
            p.name = form.cleaned_data['name']
            p.expire = form.cleaned_data['expire']
            p.nb = form.cleaned_data['number']
            p.calorie = 0  # TODO
            p.position = Position(0, 0)  # TODO
            p.save()

            return redirect('sf:new')
        else:  # ie. not valid
            c = {
                'form': form,
            }
            return render(request, 'sf/new.html', c)

    return render(request, 'sf/new.html')


# montrer la liste
def show_list(request):
    p = Product.objects.order_by('name')

    c = {
        'products': p,
    }

    return render(request, 'sf/show_list.html', c)


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
            pos = form.cleaned_data['position']
            if name and pos:
                p = Product.objects.filter(name=name, position__x=pos.x, position__y=pos.y)
            elif name:
                p = Product.objects.filter(name=name)
            elif pos:
                p = Product.objects.filter(position__x=pos.x, position__y=pos.y)

            c = {
                'product': p,
            }
            return render(request, 'sf/find_product.html', c)
        else:  # ie. not valid
            c = {
                'form': form,
            }
            return render(request, 'sf/find_product.html', c)

    return render(request, 'sf/find_product.html')

# sortir un produit + liaison serie
def get(request):
    return render(request, 'sf/get.html')

# trouver recette
def find_recipe(request):
    return render(request, 'sf/find_recipe.html')


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
