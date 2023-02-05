"""amzstock URL Configuration

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
from django.urls import include, path
#cust
from django.views.generic import TemplateView

urlpatterns = [
    
    path('admin/', admin.site.urls, name='admin_page'),
    #cust-allauth
    path('accounts/', include('allauth.urls')),
    #path('polls/', include('polls.urls')),
    path('', include('polls.urls'), name='home'),

    path('sum/', include('smartUserManagement.urls')),
    #for language changes
    path('/i18n/setlang/', include('django.conf.urls.i18n')),

    path('rosetta/', include('rosetta.urls'))
]
