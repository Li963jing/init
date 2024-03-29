"""installDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Insta.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Insta.urls')),
    path('auth/',include('django.contrib.auth.urls')),  
    #  必须在templates下创建一个叫registration的文件夹，然后在下面新建一个login.html用于登录  
    path('auth/signup/',SignUpView.as_view(),name="signup"),
]
