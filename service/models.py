from django.db.models.deletion import CASCADE
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.db import models
from django.urls import reverse
from solutioncategory.models import Category

# Create your models here.

class Service(models.Model):
    service_name=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    small_service_description=models.TextField(max_length=500, blank=True)
    service_description=models.TextField(max_length=500, blank=True)
    price=models.FloatField()
    is_available=models.BooleanField(default=True)
    images=models.ImageField(upload_to='photos/service')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_name

