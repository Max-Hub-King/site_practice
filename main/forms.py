from django import forms
from .models import NotesDjango, NotesFlask,NotesGL,NotesNew,NotesPygame,NotesPyqt5

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)

class NotesFormDjango(forms.ModelForm):
    data_django = forms.CharField(max_length=10000, required=True, label='',
    widget=forms.Textarea(attrs={
        'placeholder': 'write your note',
        'class': 'format_of_write_data',
    }))
    class Meta:
        model = NotesDjango
        fields = [
            'data_django',
        ]

class NotesFormFlask(forms.ModelForm):
    data_flask = forms.CharField(max_length=10000, required=True, label='', 
    widget=forms.Textarea(attrs={
        'placeholder': 'write your note',
        'class': 'format_of_write_data',
    }))
    class Meta:
        model = NotesFlask
        fields = [
            'data_flask',
        ]

class NotesFormPygame(forms.ModelForm):
    data_pygame = forms.CharField(max_length=10000, required=True, label='', 
    widget=forms.Textarea(attrs={
        'placeholder': 'write your note',
        'class': 'format_of_write_data',
    }))
    class Meta:
        model = NotesPygame
        fields = [
            'data_pygame',
        ]

class NotesFormGL(forms.ModelForm):
    data_git_linux = forms.CharField(max_length=10000, required=True, label='', 
    widget=forms.Textarea(attrs={
        'placeholder': 'write your note',
        'class': 'format_of_write_data',
    }))
    class Meta:
        model = NotesGL
        fields = [
            'data_git_linux',
        ]

class NotesFormPyqt5(forms.ModelForm):
    data_pyqt5 = forms.CharField(max_length=10000, required=True, label='', 
    widget=forms.Textarea(attrs={
        'placeholder': 'write your note',
        'class': 'format_of_write_data',
    }))
    class Meta:
        model = NotesPyqt5
        fields = [

            'data_pyqt5',
        ]

class NotesFormNew(forms.ModelForm):
    data_new = forms.CharField(max_length=10000, required=True, label='', 
    widget=forms.Textarea(attrs={
        'placeholder': 'write your note',
        'class': 'format_of_write_data',
    }))
    class Meta:
        model = NotesNew
        fields = [
            'data_new',
        ]