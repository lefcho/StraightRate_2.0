from django import forms
from StraightRate_2.creators.models import Director, Developer


class DirectorBaseForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Last name'}),
        }
        labels = {
            'first_name': '',
            'last_name': '',
        }


class DeveloperBaseForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'
        widgets = {
            'developer_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Developer Name'}),
            'website': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Website(optional)'}),
        }
        labels = {
            'developer_name': '',
            'website': '',
        }


class DirectorCreateForm(DirectorBaseForm):
    pass


class DeveloperCreateForm(DeveloperBaseForm):
    pass
