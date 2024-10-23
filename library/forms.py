from django.forms import ModelForm
from .models import Library

class Libraryform(ModelForm): 
    class Meta:
        model = Library
        fields = "__all__"