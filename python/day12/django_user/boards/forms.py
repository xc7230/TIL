from django import forms
from .models import Board, Comment


#model이름에 + form
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title','content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
