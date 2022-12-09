from django.urls import path
from . import views

app_name = "profile"

urlpatterns = [
    path('', views.profile, name='profile'),
    path('biography/', views.biography, name='biography'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
