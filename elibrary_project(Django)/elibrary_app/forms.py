from django import forms
from .models import EBooksModel
from .models import Category
from django.core.validators import MinLengthValidator

class EBooksForm(forms.ModelForm):
    
    class Meta:
        model = EBooksModel
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(EBooksForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter title'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter summary'})
        self.fields['pages'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter pages'})
        self.fields['pdf'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter pdf'})
        self.fields['author'].widget.attrs.update({'class': 'form-control','placeholder':'Enter author'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
    

        # Make all fields required
        for field_name, field in self.fields.items():
            field.required = True