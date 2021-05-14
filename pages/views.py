from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Page


# Create your views here.
def page(request: HttpResponse, page_id: int) -> render:

    pages = get_object_or_404(Page, id=page_id)
    context = {
        'pages': pages
    }
    return render(request=request, template_name="pages/sample.html", context=context)

