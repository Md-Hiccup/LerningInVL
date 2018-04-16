from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post            # form Model i.e CharField, TextField, DateTimeField etc
        fields = ('title', 'text',  )     # Field that shown on 
