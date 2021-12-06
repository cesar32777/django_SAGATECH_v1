import solutioncategory
from service.models import Service
from solutioncategory.models import Category
from django.shortcuts import get_object_or_404, render

def services(request, category_slug=None):
    categories=None
    services=None
    if category_slug!=None:
        categories=get_object_or_404(Category, slug=category_slug)
        services=Service.objects.filter(category=categories, is_available=True)
    else:
        services=Service.objects.all().filter(is_available=True)
        categories=Category.objects.all().filter()
    context={
        'services': services,
        'categories': categories,
    }
    return render(request, 'services.html', context)
