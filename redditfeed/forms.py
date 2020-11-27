from django import forms
from django.forms import widgets  

from .models import News

class NewsForm(forms.Form):
    text = forms.CharField(label='Your name', max_length=100)


class newsForm(forms.ModelForm):
  
    class Meta:
        model = Employee
        fields = ([
        'text', 
        'image', 
        'video',])

