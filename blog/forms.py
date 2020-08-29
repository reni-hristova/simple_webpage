from django import forms
from .models import Post, Entry

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('positionTitle', 'organisation', 'description',  'start_date', 'end_date',)
