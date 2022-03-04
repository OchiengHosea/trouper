import email
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model

from base.models import BaseModel


User = get_user_model()

class Artist(BaseModel):
    full_name = models.CharField(max_length=225)
    stage_name = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    work_phone = models.CharField(max_length=13)
    physical_address = models.CharField(max_length=125)
    user = models.ForeignKey(User, on_delete=models.CASCADE)