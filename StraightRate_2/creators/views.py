from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from StraightRate_2.creators.forms import DirectorCreateForm, DeveloperCreateForm
from StraightRate_2.creators.models import Director, Developer


class AddDirectorView(PermissionRequiredMixin, CreateView):
    model = Director
    form_class = DirectorCreateForm
    template_name = 'directors/add-director.html'
    success_url = reverse_lazy('suggest-movie')
    permission_required = 'media.can_suggest_movies'

    def handle_no_permission(self):
        return redirect('home')


class AddDeveloperView(PermissionRequiredMixin, CreateView):
    model = Developer
    form_class = DeveloperCreateForm
    template_name = 'developers/add-developer.html'
    success_url = reverse_lazy('suggest-game')
    permission_required = 'media.can_suggest_games'

    def handle_no_permission(self):
        return redirect('home')


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'directors/director-details.html'
    context_object_name = 'director'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = self.object.movies.filter(approved=True)
        return context


class DeveloperDetailView(DetailView):
    model = Developer
    template_name = 'developers/developer-details.html'
    context_object_name = 'developer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = self.object.games.filter(approved=True)
        return context
