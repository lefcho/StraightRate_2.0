from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from StraightRate_2.accounts.forms import RegisterForm, LoginForm, AppUserChangeForm
from StraightRate_2.reviews.models import MovieReview, VideoGameReview
from StraightRate_2.utils import calculate_user_points, update_user_groups

UserModel = get_user_model()


class RegisterView(CreateView):
    template_name = 'users/create-user.html'
    model = UserModel
    success_url = reverse_lazy('home')
    form_class = RegisterForm

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'users/view-profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_reviews'] = MovieReview.objects.filter(user=self.request.user)
        context['video_game_reviews'] = VideoGameReview.objects.filter(user=self.request.user)
        context['form'] = AppUserChangeForm(instance=self.request.user)

        return context

    def get(self, request, *args, **kwargs):
        calculate_user_points(self.request.user)
        update_user_groups(self.request.user)
        return super().get(request, *args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = AppUserChangeForm
    success_url = reverse_lazy('view-profile')

    def get_object(self, queryset=None):
        return self.request.user

