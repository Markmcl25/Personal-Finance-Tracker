from django.contrib import admin
from django.urls import path, include
from tracker import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Default login/logout URLs
    path('signup/', views.signup, name='signup'),  # Custom signup view
    path('', include('tracker.urls')),  # The app URLs should be included here without conflicting routes
]
