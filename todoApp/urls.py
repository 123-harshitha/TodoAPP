"""
URL configuration for todoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings, views

urlpatterns = [
    path('todos/', include('todos.urls')),
    path('admin/', admin.site.urls),
    path('', views.index)              
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)        #This allows user-uploaded media files (like images, profile pics, etc.)                                                                      # to be accessible during development.
urlpatterns += staticfiles_urlpatterns()                                 #to be accessible during the development
