from django.db.models.deletion import CASCADE
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.db import models
from django.urls import reverse

# Create your models here.

class BranchOffice(models.Model):
    branch_office_name=models.CharField(max_length=200, unique=True)
    branch_office_address=models.CharField(max_length=200, blank=True)
    is_available=models.BooleanField(default=True)
    images=models.ImageField(upload_to='photos/branchoffice')
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.branch_office_name