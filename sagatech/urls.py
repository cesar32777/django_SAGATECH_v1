"""sagatech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .import views
from django.conf.urls.static import static
from sagatech import settings

urlpatterns = [
    path('admin/', admin.site.urls), 
    path(r'^$', views.home, name="home"),#inicio/
    path('soluciones-en-informatica/', views.soluciones_informatica_home, name="soluciones_informatica_home"),
    path('mantenimiento_regular/', views.inf_mant, name="inf_mant"),
    path('servicio_a_negocios/', views.inf_servneg, name="inf_servneg"),
    path('reparacion/', views.inf_repar, name="inf_repar"),
    path('software/', views.inf_softw, name="inf_softw"),
    path('mejoras/', views.inf_mejoras, name="inf_mejoras"),
    path('armamos_tu_pc/', views.inf_pc_build, name="inf_pc_build"),
    path('soluciones-en-refrigeracion/', views.soluciones_refrigeracion_home, name="soluciones_refrigeracion_home"),
    path('mantenimiento_preventivo/', views.ref_mant_prev, name="ref_mant_prev"),
    path('mantenimiento_correctivo/', views.ref_mant_correct, name="ref_mant_correct"),
    path('instalacion_de_minisplits/', views.ref_inst_minisplit, name="ref_inst_minisplit"),
    path('about/', views.about, name="about"),
    path('services/', include('service.urls')),
    path('contact/', include('contacto.urls')),
    #path('blog/', views.blog, name="blog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
