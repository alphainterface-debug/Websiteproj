"""DEMOproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from DEMOApp import views
admin.site.site_header = "NatWest Admin"
admin.site.site_title = "NatWest Admin Portal"
admin.site.index_title = "Welcome to NatWest Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DEMOApp.urls')),
    path(r'viewcontacts/',views.contlist.as_view()),
    path(r'viewscores/',views.custlist.as_view()),
    path(r'viewsurvey/',views.surveylist.as_view()),
]
