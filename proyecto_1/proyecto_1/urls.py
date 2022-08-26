"""proyecto_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import probando_html
from app_family.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicio/", probando_html),
    path("app_family/hermano/", hermano),
    path("app_family/hermana/", hermana),
    path("app_family/madre/", madre),
    path("app_family/padre/", padre)
]
