from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    try:
        product = Product.objects.filter(pk=0).first()
    except ObjectDoesNotExist:
        pass

    return render(request, 'hello.html', {'name': 'Mosh'})
