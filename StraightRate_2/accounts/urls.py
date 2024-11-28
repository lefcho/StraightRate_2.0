from django.contrib.auth.views import LogoutView
from django.urls import path

from StraightRate_2.accounts import views

urlpatterns = (
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('view-profile/', views.ViewProfileView.as_view(), name='view-profile'),
)