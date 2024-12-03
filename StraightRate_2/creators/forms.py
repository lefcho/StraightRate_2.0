from django import forms
from StraightRate_2.creators.models import Director, Developer


class DirectorBaseForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'


class DeveloperBaseForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'


class DirectorCreateForm(DirectorBaseForm):
    pass


class DeveloperCreateForm(DeveloperBaseForm):
    pass
