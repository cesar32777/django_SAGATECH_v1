from service.models import Service
from branchoffice.models import BranchOffice
from django.shortcuts import render

from solutioncategory.models import Category

def soluciones_informatica_home(request):
    services=Service.objects.all().filter(is_available=True)
    categories=Category.objects.all()
    branchoffices=BranchOffice.objects.all().filter(is_available=True)
    context={
        'services': services,
        'branchoffices': branchoffices,
        'categories': categories,
    }
    return render(request, 'sol_inf_home.html', context)

def inf_mant(request):
    services=Service.objects.all().filter(is_available=True)
    categories=Category.objects.all()
    branchoffices=BranchOffice.objects.all().filter(is_available=True)
    context={
        'services': services,
        'branchoffices': branchoffices,
        'categories': categories,
    }
    return render(request, 'soluciones_inf/mantenimiento_regular.html', context)

def inf_servneg(request):
    services=Service.objects.all().filter(is_available=True)
    categories=Category.objects.all()
    branchoffices=BranchOffice.objects.all().filter(is_available=True)
    context={
        'services': services,
        'branchoffices': branchoffices,
        'categories': categories,
    }
    return render(request, 'soluciones_inf/servicio_negocios.html', context)

def inf_repar(request):
    services=Service.objects.all().filter(is_available=True)
    categories=Category.objects.all()
    branchoffices=BranchOffice.objects.all().filter(is_available=True)
    context={
        'services': services,
        'branchoffices': branchoffices,
        'categories': categories,
    }
    return render(request, 'soluciones_inf/reparacion.html', context)

def inf_softw(request):
    services=Service.objects.all().filter(is_available=True)
    categories=Category.objects.all()
    branchoffices=BranchOffice.objects.all().filter(is_available=True)
    context={
        'services': services,
        'branchoffices': branchoffices,
        'categories': categories,
    }
    return render(request, 'soluciones_inf/instalacion_software.html', context)

def inf_mejoras(request):
    services=Service.objects.all().filter(is_available=True)
    categories=Category.objects.all()
    branchoffices=BranchOffice.objects.all().filter(is_available=True)
    context={
        'services': services,
        'branchoffices': branchoffices,
        'categories': categories,
    }
    return render(request, 'soluciones_inf/mejoras.html', context)

def inf_pc_build(request):
    services=Service.objects.all().filter(is_available=True)
    categories=Category.objects.all()
    branchoffices=BranchOffice.objects.all().filter(is_available=True)
    context={
        'services': services,
        'branchoffices': branchoffices,
        'categories': categories,
    }
    return render(request, 'soluciones_inf/pc_build.html', context)

def home(request):
    services=Service.objects.all().filter(is_available=True)
    categories=Category.objects.all()
    branchoffices=BranchOffice.objects.all().filter(is_available=True)
    context={
        'services': services,
        'branchoffices': branchoffices,
        'categories': categories,
    }
    return render(request, 'home.html', context)

def soluciones_refrigeracion_home(request):
    services=Service.objects.all().filter(is_available=True)
    categories=Category.objects.all()
    branchoffices=BranchOffice.objects.all().filter(is_available=True)
    context={
        'services': services,
        'branchoffices': branchoffices,
        'categories': categories,
    }
    return render(request, 'sol_ref_home.html', context)

def ref_mant_prev(request):
    services=Service.objects.all().filter(is_available=True)
    categories=Category.objects.all()
    branchoffices=BranchOffice.objects.all().filter(is_available=True)
    context={
        'services': services,
        'branchoffices': branchoffices,
        'categories': categories,
    }
    return render(request, 'ref_soluciones/mantenimiento_preventivo.html', context)

def ref_mant_correct(request):
    services=Service.objects.all().filter(is_available=True)
    categories=Category.objects.all()
    branchoffices=BranchOffice.objects.all().filter(is_available=True)
    context={
        'services': services,
        'branchoffices': branchoffices,
        'categories': categories,
    }
    return render(request, 'ref_soluciones/mantenimiento_correctivo.html', context)

def ref_inst_minisplit(request):
    services=Service.objects.all().filter(is_available=True)
    categories=Category.objects.all()
    branchoffices=BranchOffice.objects.all().filter(is_available=True)
    context={
        'services': services,
        'branchoffices': branchoffices,
        'categories': categories,
    }
    return render(request, 'ref_soluciones/instalacion_minisplit.html', context)

def about(request):
    context={

    }
    return render(request, 'about.html', context)


'''
def blog(request):
    context={

    }
    return render(request, 'blog.html', context)
'''


