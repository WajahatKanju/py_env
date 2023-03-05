"""test_project URL Configuration

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
import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse
from django.views.static import serve
from django.template import loader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'pages')

def index(request):
        template = loader.get_template('test_project/main.html')
        context = {'title': 'Home'}
        return HttpResponse(template.render(context, request))

def css(request):
        template = loader.get_template('css/index.html')
        context = {'title': 'ae128a'}
        return HttpResponse(template.render(context, request))

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='home'),
    path('css/', css, name='css'),
    re_path(r'^pages/(?P<path>.*)$', serve, {'document_root': SITE_ROOT, 'show_indexes': True}, name='site_path'),
    path('polls/', include('polls.urls')),
    path('hello/', include('hello.urls')),
    path('autos/', include('autos.urls'))
]
