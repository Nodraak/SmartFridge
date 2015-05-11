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

    number = forms.IntegerField(
        label='Nombre',
        initial=1,
    )

    expire = forms.DateField(
        label='Date de péremption ',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'jj/mm/aaaa'
            }
        ),
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
                self._errors['name'] = self.error_class([msg])
            elif count > 1:
                msg = 'Plusieurs produits trouvés.'
                self._errors['name'] = self.error_class([msg])

        return cleaned_data
