# my_django_app/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include accounts app URLs
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),  # Redirect root URL to login
]