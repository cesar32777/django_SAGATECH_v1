from django.urls import path
from django.conf.urls.static import static
from sagatech import settings
from . import views

urlpatterns = [
    path('', views.categories, name='categories'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)