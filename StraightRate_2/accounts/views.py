from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from StraightRate_2.accounts.forms import RegisterForm, LoginForm, AppUserChangeForm

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


class ViewProfileView(LoginRequiredMixin, DetailView):
    template_name = 'users/view-profile.html'
    model = UserModel
