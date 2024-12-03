from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from StraightRate_2.creators.forms import DirectorCreateForm, DeveloperCreateForm
from StraightRate_2.creators.models import Director, Developer


class AddDirectorView(LoginRequiredMixin, CreateView):
    model = Director
    form_class = DirectorCreateForm
    template_name = 'directors/add-director.html'
    success_url = reverse_lazy('suggest-movie')


class AddDeveloperView(LoginRequiredMixin, CreateView):
    model = Developer
    form_class = DeveloperCreateForm
    template_name = 'developers/add-developer.html'
    success_url = reverse_lazy('suggest-game')