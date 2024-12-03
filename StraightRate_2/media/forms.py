from django import forms

from StraightRate_2.media.models import Movie


class MovieBaseForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['approved']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie title'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter description'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genres': forms.SelectMultiple(attrs={'class': 'form-control custom-select'}),
            'directors': forms.SelectMultiple(attrs={'class': 'form-control custom_select'}),
        }


class MovieCreateForm(MovieBaseForm):
    pass
