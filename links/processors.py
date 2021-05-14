from django.shortcuts import HttpResponse
from .models import Link


def context_dict(request: HttpResponse):
    context = {}
    links = Link.objects.all()
    for item in links:
        context[item.key] = item.url
    return context

