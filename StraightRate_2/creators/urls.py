from django.urls import path

from StraightRate_2.creators import views

urlpatterns = [
    path('add-director/', views.AddDirectorView.as_view(), name='add-director'),
    path('add-developer/', views.AddDeveloperView.as_view(), name='add-developer'),

]