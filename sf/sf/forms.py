#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from .models import Product


class NewForm(forms.Form):

    name = forms.CharField(
        label='Nom',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Biere'
            }
        ),
    )

    number = forms.PositiveSmallIntegerField(
        label='Nombre',
        initial=1,
    )

    expire = forms.DateField(
        label='Date de péremption ',
    )


class FindForm(forms.Form):

    name = forms.CharField(
        label='Nom',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Biere'
            }
        ),
        required=False,
    )

    position = forms.CharField(
        label='Position',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'x;y'
            }
        ),
        required=False,
    )

    retrieve = forms.BooleanField(
        label='Recuperer',
        required=False
    )

    def clean(self):
        cleaned_data = super(FindForm, self).clean()

        name = cleaned_data.get('name')
        if name:
            count = Product.objects.filter(name=name).count()
            msg = ''
            if count == 0:
                msg = 'Aucun produit trouvé.'
            elif count > 1:
                msg = 'Plusieurs produits trouvés.'
            self._errors['name'] = self.error_class([msg])

        position = cleaned_data.get('position')
        if position:
            px, py = [int(i) for i in position.split(';')]
            if Product.objects.filter(position__x=px, position__y=py).count() != 1:
                msg = 'Produit non trouvé.'
                self._errors['position'] = self.error_class([msg])

        return cleaned_data
