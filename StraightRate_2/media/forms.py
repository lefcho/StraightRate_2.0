from django import forms
from StraightRate_2.media.models import Movie, VideoGame


class MovieBaseForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['approved', 'date_added']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter movie title'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter description'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genres': forms.SelectMultiple(attrs={'class': 'form-control custom-select'}),
            'directors': forms.SelectMultiple(attrs={'class': 'form-control custom_select'}),
        }


class VideoGameBaseForm(forms.ModelForm):
    class Meta:
        model = VideoGame
        exclude = ['approved', 'date_added']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter video game title'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter description'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genres': forms.SelectMultiple(attrs={'class': 'form-control custom-select'}),
            'developer': forms.Select(attrs={'class': 'form-control'}),
        }


class MovieCreateForm(MovieBaseForm):
    pass


class VideoGameCreateForm(VideoGameBaseForm):
    pass
