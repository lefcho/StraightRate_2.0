from django.urls import path

from StraightRate_2.common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]