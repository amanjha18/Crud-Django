from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 1. Business must capture Name, address, owner info, employee size

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    capture_name = models.CharField(max_length=255)
    address = models.TextField()
    owner_info = models.CharField(max_length=255)
    employee_size = models.CharField(max_length=255)
