"""sewpat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from .views import main_view

from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('', main_view),
    path('admin/', admin.site.urls),
    path('api/', include('sewpatd.urls', namespace='api')),
    path('token-auth/', auth_views.obtain_auth_token),
    path('api-auth/', include("rest_framework.urls")),
]
