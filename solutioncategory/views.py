from solutioncategory.models import Category
from django.shortcuts import render

def categories(request):
    categories=Category.objects.all().filter()
    context={
        'categories': categories,
    }
    return render(request, 'index.html', context)