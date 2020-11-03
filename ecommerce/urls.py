"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
admin.site.site_header="iCoder Admin"
admin.site.site_title='iCoder Admin Panel'
admin.site.index_title='Welcome to iCoder Admin Panel'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Home'),
    path('shop/', include('website.urls')),
    path('blog/', include('blog.urls')),
    path('signup/', views.handleSignup, name='handleSignup'),
    path('login/', views.handleLogin, name='handlelogin'),
    path('logout/', views.handleLogout, name='handlelogout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
