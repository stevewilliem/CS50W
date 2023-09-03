from django import forms

from .models import *

forms.ModelForm

class listingForm(forms.ModelForm):
    class Meta:
        model = auction
        fields = ['title', 'description', 'bid_value', 'image', 'category', 'active_status']
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px;',
                'placeholder' : 'title'
                }),
            'description' : forms.TextInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px;',
                'placeholder' : 'description'
                }),
            'bid_value' : forms.NumberInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px;',
                'placeholder' : 'bid value'
                }),
            # 'image' : forms.URLInput(attrs={
            #     'class' : "form-control",
            #     'style' : 'max-width: 300px;',
            #     'placeholder' : 'image link'
            #     }),
            'category' : forms.TextInput(attrs={
                'class' : "form-control",
                'style' : 'max-width: 300px;',
                'placeholder' : 'category'
                }),
            'active_status' : forms.CheckboxInput()
        }