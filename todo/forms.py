from django.forms import ModelForm
from .models import TodoData


class TodoDataForm(ModelForm):
    class Meta:
        model = TodoData
        fields = ['title','description','status']
    
