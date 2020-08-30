from django import forms
from .models import Post, Entry, EducationEntry, PersonalProfile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('type', 'title', 'organisation', 'description',  'start_date', 'end_date',)

class EducationEntryForm(forms.ModelForm):
    class Meta:
        model = EducationEntry
        fields = ('degreeTitle', 'organisation', 'description',  'start_date', 'end_date',)

class PersonalProfileForm(forms.ModelForm):
    class Meta:
        model = PersonalProfile
        fields = ('description',)
