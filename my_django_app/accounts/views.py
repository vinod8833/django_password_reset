# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm, CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import MultipleObjectsReturned
from django.core.mail import send_mail  # Import if you are sending emails
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def password_reset_view(request):
    # Implement password reset logic here
    return render(request, 'registration/password_reset.html')

@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in after password change
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('dashboard')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'registration/password_change.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'username': request.user.username})

@login_required
def profile_view(request ):
    return render(request, 'registration/profile.html', {
        'username': request.user.username,
        'email': request.user.email,
        'date_joined': request.user.date_joined,
        'last_login': request.user.last_login,
    })


def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')





# accounts/views.py



def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                email_template_name='accounts/password_reset_email.html'  # Email template for sending reset instructions
            )
            return render(request, 'accounts/password_reset_done.html')  # Optional: success page
    else:
        form = PasswordResetForm()
    
    return render(request, 'accounts/password_reset.html', {'form': form})


