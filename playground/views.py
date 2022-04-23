from django.forms import DecimalField
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Product
from tags.models import TaggedItem


def say_hello(request):

    collection = Collection()
    collection.title = 'Video Games'

    return render(request, 'hello.html', {'name': 'Mosh', 'orders': list(queryset)})
