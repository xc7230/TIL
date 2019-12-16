from django import forms
from .models import Board, Comment


#model이름에 + form
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title','content']
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['title'].widget.attrs.update(
                {'class':'form-control-sm','id':'abcdef'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['comment'].widget.attrs.update(
                {
                'class':'form-control-sm', 
                'id':'abcdef'
                }
                )
