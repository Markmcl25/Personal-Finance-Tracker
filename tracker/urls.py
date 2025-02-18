from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard view as the homepage after login
    # Additional URLs for tracker-specific views can be added here
]
