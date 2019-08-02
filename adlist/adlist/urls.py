"""adlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),  # Keep
    path('ads/', include('ads.urls')),  # Keep
    path('admin/', admin.site.urls),  # Keep
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    # path('ads/', include('ads.urls')),  # Keep

    # Sample applications
    # path('owner/', include('owner.urls')),
    path('autos/', include('autos.urls')),
]


# Keep everything below this line

if 'crispy_forms' in settings.INSTALLED_APPS :
    urlpatterns += [
        path('crispy/', include('crispy.urls')),
    ]

if 'rest_framework' in settings.INSTALLED_APPS :
    urlpatterns += [
        path('rest/', include('rest.urls')),
    ]

if 'social_django' in settings.INSTALLED_APPS :
    urlpatterns += [
        url(r'^oauth/', include('social_django.urls', namespace='social')),
    ]

# Serve the favicon
import os
from django.views.static import serve
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

