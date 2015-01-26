#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'sf/index.html')

# trouver si produit est ds le frigo
def is_in_fridge(request):
    return render(request, 'sf/is_in_fridge.html')

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
    return render(request, 'sf/show_list.html')

# trouver les produits associés a la recette
# TODO
