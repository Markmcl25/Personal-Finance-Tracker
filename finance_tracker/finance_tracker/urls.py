from django.contrib import admin
from django.urls import path, include
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),  # Include app-specific URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Default login/logout URLs
    path('signup/', views.signup, name='signup'),  # Custom signup view
    path('', views.dashboard, name='dashboard'),  # Set dashboard as the homepage after login
]
