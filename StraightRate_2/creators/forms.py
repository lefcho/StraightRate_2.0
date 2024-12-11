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

    def save(self, commit=True):
        director = super().save(commit=False)

        director.first_name = director.first_name.lower().capitalize().strip()
        director.last_name = director.last_name.lower().capitalize().strip()

        if commit:
            director.save()

        return director


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

    def save(self, commit=True):
        developer = super().save(commit=False)

        developer.developer_name = developer.developer_name.strip()

        if commit:
            developer.save()

        return developer


class DirectorCreateForm(DirectorBaseForm):
    pass


class DeveloperCreateForm(DeveloperBaseForm):
    pass
