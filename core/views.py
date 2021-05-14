from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request: HttpResponse) -> render:
    return render(request, "core/home.html")


def about(request: HttpResponse) -> render:
    return render(request, "core/about.html")


def store(request: HttpResponse) -> render:
    return render(request, "core/store.html")

