from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from StraightRate_2.accounts.forms import AppUserChangeForm, RegisterForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    model = UserModel
    add_form = RegisterForm
    form = AppUserChangeForm

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )