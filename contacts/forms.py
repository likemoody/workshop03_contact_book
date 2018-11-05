from django import forms
from django.forms.models import ModelForm
from .models import Person


class PersonAddForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'description', 'profile_img', 'group']
        widgets = {
            'group': forms.CheckboxSelectMultiple,
        }


class GroupForm(forms.Form):
    name = forms.CharField(label='Group name', max_length=32)
