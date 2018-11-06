from django import forms
from .models import Person


class PersonAddForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'description', 'profile_img', 'group']
        widgets = {
            'group': forms.CheckboxSelectMultiple(attrs={'class': 'list_no_disc'}),
        }


class GroupForm(forms.Form):
    name = forms.CharField(label='Group name', max_length=32)


class SearchForm(forms.Form):
    first_name = forms.CharField(label='First name',
                                 max_length=32,
                                 required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'First name'}))

    last_name = forms.CharField(label='Last name',
                                max_length=32,
                                required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Last name'}))

