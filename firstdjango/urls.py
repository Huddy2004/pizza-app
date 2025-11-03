from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstdjango.urls')),  # Include URLs from the firstdjango app
    path('accounts/', include('django.contrib.auth.urls')),  # Include default Django authentication URLs
]
