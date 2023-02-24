from django.db import models
from django.contrib.auth.models import User

import uuid
# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False ,default=uuid.uuid4)
    class Meta:
        abstract = True

class TodoData(BaseModel):
    status_choices = [
        ('C' , 'COMPLETED'),
        ('P' , 'PENDING'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=2,choices=status_choices)
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title

