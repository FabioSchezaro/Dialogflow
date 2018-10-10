from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('webhook/', include('webhook.urls')),
    path('admin/', admin.site.urls),
]
