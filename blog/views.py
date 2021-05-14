from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Post, Category


# Create your views here.
def blog(request: HttpResponse) -> HttpResponse:
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request=request, template_name="blog/blog.html", context=context)


def category(request: HttpResponse, category_id: int) -> HttpResponse:
    categories = get_object_or_404(Category, id=category_id)  # Adds an error 404
    # posts = Post.objects.filter(categories=category)
    context = {
        'categories': categories
    }
    return render(request=request, template_name="blog/category.html", context=context)

