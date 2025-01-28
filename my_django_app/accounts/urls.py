# accounts/urls.py

from django.urls import path  # Make sure to import path
from . import views
from .views import password_reset_view


urlpatterns = [
    path('', views.home_view, name='home'),  # Home view
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    path('password_change/', views.password_change_view, name='password_change'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),  # Add logout URL
    path('password_reset/', views.password_reset_view, name='password_reset'),

]