from django.urls import path
from django.conf.urls.static import static
from sagatech import settings
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('category/<slug:category_slug>/', views.services, name='service_by_category'),

]