from django.contrib import admin
from django.urls import path, include
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),  # This includes the tracker app's URL patterns
    path('accounts/', include('django.contrib.auth.urls')),  # Default login/logout URLs
    path('signup/', views.signup, name='signup'),  # Custom signup view
]
