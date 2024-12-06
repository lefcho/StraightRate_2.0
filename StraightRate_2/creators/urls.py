from django.urls import path

from StraightRate_2.creators import views

urlpatterns = [
    path('add-director/', views.AddDirectorView.as_view(), name='add-director'),
    path('add-developer/', views.AddDeveloperView.as_view(), name='add-developer'),
    path('developer/<int:pk>/', views.DeveloperDetailView.as_view(), name='developer-details'),
    path('director/<int:pk>/', views.DirectorDetailView.as_view(), name='director-details'),

]