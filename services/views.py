from django.shortcuts import render, HttpResponse
from .models import Service


# Create your views here.
def services(request: HttpResponse) -> render:
    """
    services = Service.object.all()
    context = {
        'services': services
    }
    """
    return render(request=request, template_name="services/services.html")

