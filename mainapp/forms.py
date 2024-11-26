from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Posts
class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['text','image']
        widgets = { 
            'text':CKEditorWidget()
        }

