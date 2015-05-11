#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from ..sf.models import Product, Position


"""
    from django.http import JsonResponse
    response = JsonResponse(dict)

    import simplejson
    dict = simplejson.loads(json)

        new : /api/new : POST : json payload :
            name : str
            expire : date
            number : int
        show_list : /api/show_list : GET, json response :
            name
            nb
            expire
"""


@csrf_exempt
def new(request):
    if request.method == 'GET':
        return HttpResponse('please post data in json format')
    elif request.method == 'POST':
        payload = simplejson.loads(request.body)

        pos = Position()  # TODO
        pos.x = 0
        pos.y = 0
        pos.save()

        print payload

        p = Product()
        p.name = payload['name']
        p.expire = payload['expire']
        p.nb = payload['nb']
        p.calorie = 0  # TODO
        p.position = pos
        p.save()

        return HttpResponse('ok')
    else:
        return HttpResponse('method not implemented')


def show_list(request):
    products = Product.objects.order_by('name')

    dict = [{'name': p.name, 'nb': p.nb, 'expire': p.expire} for p in products]
    return JsonResponse(dict, safe=False)
