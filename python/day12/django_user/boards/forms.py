from django import forms
from .models import Board


#model이름에 + form
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title','content']
